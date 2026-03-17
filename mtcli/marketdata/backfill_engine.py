"""
BackfillEngine

Carrega ticks históricos do MetaTrader5.
"""

import datetime
import MetaTrader5 as mt5

from mtcli.logger import setup_logger
from mtcli.mt5_context import mt5_conexao

logger = setup_logger(__name__)


class BackfillEngine:

    WINDOW_MINUTES = 10

    def __init__(self, symbol, tick_bus, repository):

        self.symbol = symbol
        self.raw_tick_bus = tick_bus
        self.repository = repository
        self.last_time_msc = None

    # ---------------------------------------------------------

    def _get_last_stored(self):

        last = self.repository._get_last_tick_msc(self.symbol)

        if last:
            logger.info(
                "Backfill retomando do último tick armazenado: %s",
                last,
            )

        return last

    # ---------------------------------------------------------

    def run(self, days=5):

        logger.info(
            "Backfill iniciado (%s) — até %s dias de histórico",
            self.symbol,
            days,
        )

        with mt5_conexao():

            mt5.symbol_select(self.symbol, True)

            now = datetime.datetime.now()

            last = self._get_last_stored()

            if last:

                self.last_time_msc = last

                start = datetime.datetime.fromtimestamp(
                    (last + 1) / 1000
                )

            else:

                start = now - datetime.timedelta(days=days)

            end = now

            total_loaded = 0

            while start < end:

                chunk_end = start + datetime.timedelta(
                    minutes=self.WINDOW_MINUTES
                )

                if chunk_end > end:
                    chunk_end = end

                ticks = mt5.copy_ticks_range(
                    self.symbol,
                    start,
                    chunk_end,
                    mt5.COPY_TICKS_ALL,
                )

                if ticks is None or len(ticks) == 0:

                    start = chunk_end
                    continue

                if self.last_time_msc:

                    mask = ticks["time_msc"] > self.last_time_msc
                    ticks = ticks[mask]

                    if len(ticks) == 0:

                        start = chunk_end
                        continue

                self.raw_tick_bus.publish_many(ticks)

                last_msc = int(ticks[-1]["time_msc"])

                if last_msc == self.last_time_msc:

                    logger.warning(
                        "Proteção de loop ativada — encerrando backfill"
                    )

                    break

                self.last_time_msc = last_msc

                total_loaded += len(ticks)

                if total_loaded % 1_000_000 < len(ticks):

                    logger.info(
                        "Backfill progresso (%s): %s ticks",
                        self.symbol,
                        f"{total_loaded:,}",
                    )

                start = chunk_end

        logger.info(
            "Backfill concluído (%s) — %s ticks processados",
            self.symbol,
            f"{total_loaded:,}",
        )

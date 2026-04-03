"""
BackfillEngine

Responsável por carregar ticks históricos do MetaTrader5
em modo batch (janela temporal) e publicá-los no pipeline
event-driven.

Características:

- Processamento incremental (retoma do último tick)
- Janela deslizante (WINDOW_MINUTES)
- Proteção contra loops
- Publicação desacoplada via TickBus

IMPORTANTE:

Este engine NÃO garante persistência direta.
Ele apenas publica eventos.

A responsabilidade de gravação é dos subscribers
(ex: TickWriter).
"""

import datetime
import MetaTrader5 as mt5

from mtcli.logger import setup_logger
from mtcli.mt5_context import mt5_conexao

logger = setup_logger(__name__)


class BackfillEngine:
    """
    Engine de backfill de ticks históricos.

    Parameters
    ----------
    symbol : str
        Símbolo a ser carregado
    tick_bus : TickBus
        Event bus onde os ticks serão publicados
    repository : TickRepository
        Repositório usado para controle incremental
    """

    WINDOW_MINUTES = 10

    def __init__(self, symbol, tick_bus, repository):

        self.symbol = symbol
        self.raw_tick_bus = tick_bus
        self.repository = repository
        self.last_time_msc = None

    # ---------------------------------------------------------

    def _get_last_stored(self):
        """
        Recupera o último tick persistido no banco.

        Returns
        -------
        int | None
            Timestamp em milissegundos do último tick
        """

        last = self.repository._get_last_tick_msc(self.symbol)

        if last:
            logger.info(
                "Backfill retomando do último tick armazenado: %s",
                last,
            )

        return last

    # ---------------------------------------------------------

    def run(self, days=5):
        """
        Executa o backfill histórico.

        Parameters
        ----------
        days : int
            Quantidade de dias retroativos
        """

        logger.info(
            "Backfill iniciado (%s) — até %s dias",
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
                        "Proteção de loop ativada — encerrando"
                    )
                    break

                self.last_time_msc = last_msc

                total_loaded += len(ticks)

                if total_loaded % 1_000_000 < len(ticks):

                    logger.info(
                        "Backfill (%s): %s ticks",
                        self.symbol,
                        f"{total_loaded:,}",
                    )

                start = chunk_end

        logger.info(
            "Backfill finalizado (%s) — %s ticks publicados",
            self.symbol,
            f"{total_loaded:,}",
        )

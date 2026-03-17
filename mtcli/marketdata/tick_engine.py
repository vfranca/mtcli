"""
TickEngine

Captura ticks continuamente do MetaTrader5
e publica no raw TickBus.
"""

import time
from datetime import datetime, timedelta
import MetaTrader5 as mt5

from mtcli.logger import setup_logger

logger = setup_logger(__name__)


class TickEngine:
    """Engine de captura contínua de ticks."""

    def __init__(self, symbol, tick_bus, poll_interval=0.2):
        self.symbol = symbol
        self.tick_bus = tick_bus
        self.poll_interval = poll_interval
        self.running = False
        self.last_time_msc = None

    def _initial_sync(self):
        """Busca ticks recentes para evitar gaps na inicialização."""
        start = datetime.now() - timedelta(minutes=5)
        end = datetime.now()

        logger.info("TickEngine initial sync (%s)", self.symbol)
        ticks = mt5.copy_ticks_range(self.symbol, start, end, mt5.COPY_TICKS_ALL)

        if ticks is None or len(ticks) == 0:
            logger.warning("Nenhum tick encontrado no sync inicial (%s)", self.symbol)
            return

        logger.info("Sync inicial carregou %d ticks (%s)", len(ticks), self.symbol)
        self.tick_bus.publish_many(ticks)
        self.last_time_msc = int(ticks[-1]["time_msc"])

    def start(self):
        """Inicia captura contínua de ticks."""
        logger.info("TickEngine start (%s)", self.symbol)
        self.running = True
        self._initial_sync()

        while self.running:
            try:
                if self.last_time_msc is None:
                    from_time = datetime.now() - timedelta(seconds=10)
                else:
                    from_time = datetime.fromtimestamp((self.last_time_msc + 1) / 1000)

                ticks = mt5.copy_ticks_from(self.symbol, from_time, 1000, mt5.COPY_TICKS_ALL)

                if ticks is None or len(ticks) == 0:
                    time.sleep(self.poll_interval)
                    continue

                # duplicação temporal
                if self.last_time_msc is not None:
                    mask = ticks["time_msc"] > self.last_time_msc
                    ticks = ticks[mask]

                if len(ticks) == 0:
                    time.sleep(self.poll_interval)
                    continue

                self.tick_bus.publish_many(ticks)
                self.last_time_msc = int(ticks[-1]["time_msc"])

            except Exception:
                logger.exception("Erro no TickEngine (%s)", self.symbol)

            time.sleep(self.poll_interval)

    def stop(self):
        """Solicita parada do engine."""
        logger.info("TickEngine stop solicitado (%s)", self.symbol)
        self.running = False

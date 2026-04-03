"""
TickEngine

Captura ticks do MetaTrader5 via polling e publica no TickBus.
"""

import time
from datetime import datetime, timedelta, timezone
import MetaTrader5 as mt5

from ..utils.time import now_utc
from ..logger import setup_logger

logger = setup_logger(__name__)


class TickEngine:

    def __init__(self, symbol, tick_bus, poll_interval=0.05):

        self.symbol = symbol
        self.tick_bus = tick_bus
        self.poll_interval = poll_interval

        self.running = False
        self.last_time_msc = None

    def start(self):

        self.running = True

        while self.running:

            try:

                if self.last_time_msc:
                    from_time = datetime.fromtimestamp(
                        (self.last_time_msc + 1) / 1000,
                        tz=timezone.utc
                    )
                else:
                    from_time = now_utc() - timedelta(seconds=2)

                ticks = mt5.copy_ticks_from(
                    self.symbol,
                    from_time,
                    1000,
                    mt5.COPY_TICKS_ALL
                )

                if ticks is None or len(ticks) == 0:
                    time.sleep(self.poll_interval)
                    self.poll_interval = min(0.2, self.poll_interval * 1.2)
                    continue

                self.tick_bus.publish_many(ticks)

                self.last_time_msc = int(ticks[-1]["time_msc"])

                # 🔥 acelera quando tem fluxo
                self.poll_interval = 0.01

            except Exception:
                logger.exception("Erro TickEngine")

                if not mt5.initialize():
                    logger.error("Tentando reconectar MT5...")
                    time.sleep(1)

    def stop(self):
        """Para engine."""
        self.running = False

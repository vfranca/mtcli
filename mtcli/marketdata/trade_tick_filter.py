"""
TradeTickFilter

Subscriber do TickBus responsável por filtrar apenas
ticks de negócio (trade ticks).
"""

import MetaTrader5 as mt5
from mtcli.logger import setup_logger

logger = setup_logger(__name__)


class TradeTickFilter:
    """
    Filtra apenas ticks que representam negócios executados.
    """

    def __init__(self, downstream_bus):
        self.downstream_bus = downstream_bus

    def __call__(self, ticks):

        if ticks is None or len(ticks) == 0:
            return

        mask = (ticks["flags"] & mt5.TICK_FLAG_LAST) != 0
        filtered = ticks[mask]

        if len(filtered) == 0:
            return

        logger.debug(
            "TradeTickFilter: %d → %d trade ticks",
            len(ticks),
            len(filtered),
        )

        self.downstream_bus.publish_many(filtered)

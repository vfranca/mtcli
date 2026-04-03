"""
TradeTickFilter

Filtra apenas ticks de negócio (LAST).
"""

import MetaTrader5 as mt5


class TradeTickFilter:

    def __init__(self, downstream_bus):
        self.downstream_bus = downstream_bus

    def __call__(self, ticks):

        mask = (ticks["flags"] & mt5.TICK_FLAG_LAST) != 0
        filtered = ticks[mask]

        if len(filtered):
            self.downstream_bus.publish_many(filtered)

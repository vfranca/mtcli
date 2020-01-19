"""
Facade para PyMQL5
"""
from PyMQL5 import PyMQL5


mql5 = PyMQL5()


class PyMQL5Facade:
    """Faxada para PyMQL5."""

    def __init__(self, symbol: str, period: str):
        self.symbol = symbol
        self.period = period

    def get_close(self) -> float:
        return mql5.iClose(self.symbol, self.period, 0)

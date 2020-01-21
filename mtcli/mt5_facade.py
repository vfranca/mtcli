"""
Facade para PyMQL5
"""
from PyMQL5 import PyMQL5
from mtcli.conf import CONNECTION_ERROR


mql5 = PyMQL5()


class MT5Facade(object):
    """ Facade para PyMQL5."""

    def __init__(self, symbol: str, period: str):
        self.symbol = symbol
        self.period = period

    def close(self) -> float:
        """ Retorna o preço de fechamento da barra."""
        res = mql5.iClose(self.symbol, self.period, 0)
        if res == None:
            raise Exception(CONNECTION_ERROR)
        return res

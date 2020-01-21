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

    def buy(
        self,
        volume: int,
        price_open: float = 0.0,
        sl: float = 0.0,
        tp: float = 0.0,
        comments: str = "",
    ) -> int:
        """ Abre uma posição comprada."""
        if not price_open:
            price_open = self.close()
        symbol = self.symbol
        res = mql5.Buy(symbol, volume, price_open, sl, tp, comments)
        if res == None:
            raise Exception(CONNECTION_ERROR)
        if res == -1:
            return 0
        return res

    def sell(
        self,
        volume: int,
        price_open: float = 0.0,
        sl: float = 0.0,
        tp: float = 0.0,
        comments: str = "",
    ) -> int:
        """ Abre uma posição vendida."""
        if not price_open:
            price_open = self.close()
        symbol = self.symbol
        res = mql5.Sell(symbol, volume, price_open, sl, tp, comments)
        if res == None:
            raise Exception(CONNECTION_ERROR)
        if res == -1:
            return 0
        return res

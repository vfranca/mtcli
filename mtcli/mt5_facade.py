"""
Facade para PyMQL5
"""
from PyMQL5 import PyMQL5
from mtcli.conf import CONNECTION_ERROR


mql5 = PyMQL5()


class MT5Facade(object):
    """ Facade para PyMQL5."""

    def __init__(self, symbol: str = "", period: str = ""):
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

    def buy_limit(
        self,
        volume: int,
        price_open: float,
        sl: float = 0.0,
        tp: float = 0.0,
        comments: str = "",
    ) -> int:
        """Abre uma posição comprada com órdem limit."""
        symbol = self.symbol
        res = mql5.BuyLimit(symbol, volume, price_open, sl, tp, comments)
        if res == None:
            raise Exception(CONNECTION_ERROR)
        if res == -1:
            return 0
        return res

    def buy_stop(
        self,
        volume: int,
        price_open: float,
        sl: float = 0.0,
        tp: float = 0.0,
        comments: str = "",
    ) -> int:
        """Abre uma posição comprada com ordem stop."""
        symbol = self.symbol
        res = mql5.BuyStop(symbol, volume, price_open, sl, tp, comments)
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

    def sell_limit(
        self,
        volume: int,
        price_open: float,
        sl: float = 0.0,
        tp: float = 0.0,
        comments: str = "",
    ) -> int:
        """Abre uma posição vendida com órdem limit."""
        symbol = self.symbol
        res = mql5.SellLimit(symbol, volume, price_open, sl, tp, comments)
        if res == None:
            raise Exception(CONNECTION_ERROR)
        if res == -1:
            return 0
        return res

    def sell_stop(
        self,
        volume: int,
        price_open: float,
        sl: float = 0.0,
        tp: float = 0.0,
        comments: str = "",
    ) -> int:
        """Abre uma posição vendida com ordem stop."""
        symbol = self.symbol
        res = mql5.SellStop(symbol, volume, price_open, sl, tp, comments)
        if res == None:
            raise Exception(CONNECTION_ERROR)
        if res == -1:
            return 0
        return res

    def orders(self) -> str:
        """Retorna todas as órdens pendentes."""
        orders = mql5.OrderAll()
        if orders == None:
            raise Exception(CONNECTION_ERROR)
        res = ""
        for o in orders:
            res += "%s %s %s %s %s %s %s\n" % (
                o["TICKET"],
                o["TYPE"],
                o["SYMBOL"],
                o["VOLUME_INITIAL"],
                o["PRICE_OPEN"],
                o["SL"],
                o["TP"],
            )
        return res

    def positions(self) -> str:
        """Retorna todas as posições abertas."""
        positions = mql5.PositionAll()
        if positions == None:
            raise Exception(CONNECTION_ERROR)
        res = ""
        for p in positions:
            res += "%s %s %s %s %s %s %s %s %s\n" % (
                p["TICKET"],
                p["SYMBOL"],
                p["TYPE"],
                p["VOLUME"],
                p["PRICE_OPEN"],
                p["SL"],
                p["TP"],
                p["PRICE_CURRENT"],
                p["TIME"],
            )
        return res

    def modify_position_symbol(self, symbol: str, sl: float, tp: float) -> bool:
        """Altera parâmetros da posição do ativo."""
        res = mql5.PositionModifySymbol(symbol, sl, tp)
        if res == None:
            raise Exception(CONNECTION_ERROR)
        return res

    def cancel_positions(self) -> bool:
        """Cancela todas as posições abertas."""
        res = mql5.CancelAllPosition()
        if res == None:
            raise Exception(CONNECTION_ERROR)
        return res

    def cancel_position_symbol(self, symbol: str) -> bool:
        """Cancela a posição do ativo."""
        res = mql5.PositionCloseSymbol(symbol)
        if res == None:
            raise Exception(CONNECTION_ERROR)
        return res

    def cancel_position_ticket(self, ticket: int) -> bool:
        """Cancela a posição do ticket."""
        res = mql5.PositionCloseTicket(ticket)
        if res == None:
            raise Exception(CONNECTION_ERROR)
        return res

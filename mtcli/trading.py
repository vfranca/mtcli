# -*- coding: utf-8 -*-
from PyMQL5 import PyMQL5
from mtcli.conf import CONNECTION_MISSING


mql5 = PyMQL5()


def get_close(symbol: str) -> float:
    """ Obtem o preço de fechamento do ativo."""
    return mql5.iClose(symbol, "daily", 0)


def info() -> str:
    """Retorna dados da conta."""
    return mql5.AccountInfoAll()


def buy(symbol: str, vol: int, sl: float, tp: float) -> int:
    """ Executa uma órdem de compra a mercado."""
    price = get_close(symbol)
    res = mql5.Buy(symbol, vol, price, sl, tp, "")
    if res < 0:
        return 0
    return res


def buy_limit(symbol: str, price: float, vol: int, sl: float, tp: float) -> int:
    """ Executa uma órdem de compra limitada."""
    res = mql5.BuyLimit(symbol, vol, price, sl, tp, "")
    if res < 0:
        return 0
    return res


def buy_stop(symbol: str, price: float, vol: int, sl: float, tp: float) -> int:
    """ Executa uma órdem de compra stop."""
    res = mql5.BuyStop(symbol, vol, price, sl, tp, "")
    if res < 0:
        return 0
    return res


def sell(symbol: str, vol: int, sl: float, tp: float) -> int:
    """ Executa uma órdem de venda a mercado."""
    price = get_close(symbol)
    res = mql5.Sell(symbol, vol, price, sl, tp, "")
    if res < 0:
        return 0
    return res


def sell_limit(symbol: str, price: float, vol: int, sl: float, tp: float) -> int:
    """ Executa uma órdem de venda limitada."""
    res = mql5.SellLimit(symbol, vol, price, sl, tp, "")
    if res < 0:
        return 0
    return res


def sell_stop(symbol: str, price: float, vol: int, sl: float, tp: float) -> int:
    """ Executa uma órdem de venda stop."""
    res = mql5.SellStop(symbol, vol, price, sl, tp, "")
    if res < 0:
        return 0
    return res


def get_total_orders() -> int:
    """Retorna o total de órdens pendentes."""
    return mql5.OrdersTotal()


def get_orders() -> str:
    """Retorna uma lista com as órdens pendentes."""
    orders = mql5.OrderAll()
    if orders == None:
        return CONNECTION_MISSING
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


def cancel_orders() -> bool:
    """Cancela todas as órdens pendentes."""
    return mql5.CancelAllOrder()


def cancel_order(ticket: int) -> bool:
    """Cancela uma ordem pelo ticket."""
    return mql5.DeleteOrder(ticket)


def get_total_positions():
    """Retorna o total de posições."""
    return mql5.PositionsTotal()


def get_positions():
    """Retorna uma lista de posições abertas."""
    positions = mql5.PositionAll()
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


def modify_position_by_symbol(symbol, stop_loss, take_profit):
    return 0


def modify_position_by_ticket(ticket, stop_loss, take_profit):
    return 0


def cancel_position_by_symbol(symbol: str) -> bool:
    """Fecha a posição do ativo passado como argumento."""
    return mql5.PositionCloseSymbol(symbol)


def cancel_position_by_ticket(ticket: int) -> bool:
    """Fecha a posição do ticket passado como argumento."""
    return mql5.PositionCloseTicket(ticket)


def cancel_positions() -> bool:
    """Fecha todas as posições abertas."""
    return mql5.CancelAllPosition()

# -*- coding: utf-8 -*-
from PyMQL5 import PyMQL5
from mtcli.conf import *


mql5 = PyMQL5()

def get_close(symbol):
    """ Obtem o preço de fechamento do ativo."""
    return mql5.iClose(symbol, "daily", 0)

def info():
    """Retorna dados da conta."""
    return mql5.AccountInfoAll()

def buy(symbol, vol=VOLUME, sl=STOP_LOSS, tp=TAKE_PROFIT):
    """ Executa uma órdem de compra a mercado."""
    price = get_close(symbol)
    sl = price - sl
    tp = price + tp
    return mql5.Buy(symbol, vol, price, sl, tp, "")

def buy_limit(symbol, price, vol=VOLUME, sl=STOP_LOSS, tp=TAKE_PROFIT):
    """ Executa uma órdem de compra limitada."""
    sl = price - sl
    tp = price + tp
    return mql5.BuyLimit(symbol, vol, price, sl, tp, "")

def buy_stop(symbol, price, vol=VOLUME, sl=STOP_LOSS, tp=TAKE_PROFIT):
    """ Executa uma órdem de compra stop."""
    sl = price - sl
    tp = price + tp
    return mql5.BuyStop(symbol, vol, price, sl, tp, "")

def sell(symbol, vol=VOLUME, sl=STOP_LOSS, tp=TAKE_PROFIT):
    """ Executa uma órdem de venda a mercado."""
    price = get_close(symbol)
    sl = price + sl
    tp = price - tp
    return mql5.Sell(symbol, vol, price, sl, tp, "")

def sell_limit(symbol, price, vol=VOLUME, sl=STOP_LOSS, tp=TAKE_PROFIT):
    """ Executa uma órdem de venda limitada."""
    sl = price + sl
    tp = price - tp
    return mql5.SellLimit(symbol, vol, price, sl, tp, "")

def sell_stop(symbol, price, vol=VOLUME, sl=STOP_LOSS, tp=TAKE_PROFIT):
    """ Executa uma órdem de venda stop."""
    sl = price + sl
    tp = price - tp
    return mql5.SellStop(symbol, vol, price, sl, tp, "")

def total_orders():
    """Retorna o total de órdens."""
    return mql5.HistoryDealTotalDay()

def total_positions():
    """Retorna o total de posições."""
    return mql5.PositionsTotal()

def positions():
    """Histórico de posições."""
    positions = mql5.HistoryDealAllDay()
    result = "Órdem | Hora | Tipo | Posição | Volume | Preço | Ativo\n"
    for p in positions:
        result += "%s %s %s %s %s %s %s\n" % (p["ORDER"], p["TIME"], p["TYPE"], p["POSITION_ID"], p["VOLUME"], p["PRICE"], p["SYMBOL"])
    return result

def modify_position_by_symbol(symbol, stop_loss, take_profit):
    return 0

def modify_position_by_ticket(ticket, stop_loss, take_profit):
    return 0

def cancel_position(symbol, volume=None):
    return 0

def cancel_orders(order=None):
    """Cancela órdens pendentes."""
    return mql5.CancelAllOrder()

def cancel_positions(position=None):
    """Cancela posições."""
    return mql5.CancelAllPosition()

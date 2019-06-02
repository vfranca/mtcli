from .fib import Fib
from cli_trade.settings import *

def get_fib(high, low, trend):
    if trend == "alta":
        trend = "h"
    elif trend == "baixa":
        trend = "l"
    else:
        trend = "h"
    return Fib(high, low, trend)

def get_trend(high, low):
    """ Retorna a tendência da sequência de dois candles."""
    if high[1] > high[0] and low[1] > low[0]:
        return lbl_asc
    if high[1] < high[0] and low[1] < low[0]:
        return lbl_desc
    if high[1] <= high[0] and low[1] >= low[0]:
        return lbl_ib
    if high[1] > high[0] and low[1] < low[0]:
        return lbl_ob
    return ""


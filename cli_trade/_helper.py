# -*- coding: utf-8 -*-
from cli_trade._fib import Fib
from cli_trade.conf import *


def get_fib(high, low, trend):
    if trend == "alta":
        trend = "h"
    elif trend == "baixa":
        trend = "l"
    else:
        trend = "h"
    return Fib(high, low, trend)

def get_medium_point(bar):
    """ Retorna o ponto médio da barra."""
    return round(bar.low + bar.range / 2, digits)

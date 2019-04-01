import csv
from .patterns import *
from .brooks_patterns import *
from .fib import Fib

lbl_asc = "ASC"
lbl_desc = "DESC"
lbl_ob = "OB"
lbl_ib = "IB"

def chart_reader(file):
    """ Lê um gráfico de barras/candlestick para uma lista."""
    f = open(file, encoding = "utf-16", newline = "")
    lines = csv.reader(f, delimiter = ',', quotechar = '\'')
    r = []
    for line in lines:
        r.append(line)
    f.close()
    return r

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


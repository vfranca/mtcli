import csv
from .patterns import *
from .brooks_patterns import BrooksPatterns
from .fib import Fib

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
        return "asc"
    if high[1] < high[0] and low[1] < low[0]:
        return "desc"
    if high[1] < high[0] and low[1] > low[0]:
        return "inside"
    if high[1] > high[0] and low[1] < low[0]:
        return "outside"
    return ""


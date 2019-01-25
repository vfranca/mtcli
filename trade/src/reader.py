import csv
from .patterns import *
from .fib import Fib

def chart_reader(filename):
    """ Lê um gráfico de barras/candlestick para uma lista.
    
    Lê um arquivo CSV exportado do MetaTrader 5
    Retorna uma lista de listas.
    Argumentos:
    filename: arquivo CSV MT5.
    """
    f = open(filename, encoding = "utf-16", newline = "")
    lines = csv.reader(f, delimiter = ',', quotechar = '\'')
    r = []
    for line in lines:
        r.append(line)
    f.close()
    return r


# Padrões complexos
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

def get_show_default(candle, **kwargs):
    """Retorna a exibição no formato padrão."""
    pattern = get_pattern(candle.body, candle.top_tail, candle.bottom_tail)
    fib = get_fib(candle.high, candle.low, candle.trend)
    if kwargs.get("trend"):
        trend = kwargs.get("trend")
    else:
        trend = ""
    if kwargs.get("complex_pattern"):
        complex_pattern = kwargs.get("complex_pattern")
    else:
        complex_pattern = ""
    return "%s %s %s %i %.1f %.1f %.1f * %.1f %.1f %.1f > %.1f %.1f %.1f" % (trend, complex_pattern, pattern, candle.body, candle.high, candle.low, candle.close, fib.r61, fib.r, fib.r38, fib.e38, fib.e, fib.e61)



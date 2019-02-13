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

def get_show_default(candle, trend, pattern2):
    """Retorna a exibição no formato padrão."""
    fib = get_fib(candle.high, candle.low, candle.trend)
    pattern = get_pattern(candle.body, candle.top_tail, candle.bottom_tail)
    return "%s %s %s %i %.0f %.0f %.0f * %.0f %.0f %.0f > %.0f %.0f %.0f" % (trend, pattern2, pattern, candle.body, candle.high, candle.low, candle.close, fib.r61, fib.r, fib.r38, fib.e38, fib.e, fib.e61)

def get_show_wdo(candle, trend, pattern2):
    """Retorna a exibição padrão para dólar."""
    fib = get_fib(candle.high, candle.low, candle.trend)
    pattern = get_pattern(candle.body, candle.top_tail, candle.bottom_tail)
    return "%s %s %s %i %.1f %.1f %.1f * %.1f %.1f %.1f > %.1f %.1f %.1f" % (trend, pattern2, pattern, candle.body, candle.high, candle.low, candle.close, fib.r61, fib.r, fib.r38, fib.e38, fib.e, fib.e61)

def get_show_stock(candle, trend, pattern2):
    """Retorna a exibição padrão para ações."""
    fib = get_fib(candle.high, candle.low, candle.trend)
    pattern = get_pattern(candle.body, candle.top_tail, candle.bottom_tail)
    return "%s %s %s %i %.2f %.2f %.2f * %.2f %.2f %.2f > %.2f %.2f %.2f" % (trend, pattern2, pattern, candle.body, candle.high, candle.low, candle.close, fib.r61, fib.r, fib.r38, fib.e38, fib.e, fib.e61)

def get_show_full(candle, trend, pattern2):
    """Retorna a exibição no formato completo."""
    pattern = get_pattern(candle.body, candle.top_tail, candle.bottom_tail)
    fib = get_fib(candle.high, candle.low, candle.trend)
    return "%s %s %s %i %i %i %.2f %.2f %.2f %.2f * %.2f %.2f %.2f > %.2f %.2f %.2f" % (trend, pattern2, pattern, candle.top_tail, candle.body, candle.bottom_tail, candle.open, candle.high, candle.low, candle.close, fib.r61, fib.r, fib.r38, fib.e38, fib.e, fib.e61)


def get_show_channel(candle, trend, lt_diff):
    """Retorna a exibição no formato de canal."""
    lt_high = candle.high + lt_diff
    lt_low = candle.low + lt_diff
    return "%s %.2f %.2f > %.2f %.2f" % (trend, candle.high, candle.low, lt_high, lt_low)

def get_lt_diff(high, low, trend):
    if trend == "asc":
        return low[1] - low[0]
    elif trend == "desc":
        return high[1] - high[0]
    else:
        return 0

def get_show_close(candle):
    """Retorna a exibição com os fechamentos."""
    return "%.2f" % candle.close

def get_show_high(candle):
    """Retorna a exibição com as máximas."""
    return "%.2f" % candle.high

def get_show_low(candle):
    """Retorna a exibição com as mínimas."""
    return "%.2f" % candle.low

def get_show_volume(candle, trend):
    """Retorna a exibição com os volumes."""
    return "%s %i" % (trend, candle.volume)

def get_show_brooks(candle, trend):
    """Retorna a exibição com os padrões de Brooks."""
    fib = get_fib(candle.high, candle.low, candle.trend)
    brooks = BrooksPatterns(candle.body)
    return "%s %s %i %i %i %.2f %.2f %.2f * %.2f > %.2f" % (trend, brooks.pattern, candle.body, candle.top_tail, candle.bottom_tail, candle.high, candle.low, candle.close, fib.r, fib.e)

def get_show_fib(candle, trend):
    """Retorna a exibição de Fibonacci."""
    fib = get_fib(candle.high, candle.low, candle.trend)
    return "%s %i %.2f %.2f %.2f > %.2f %.2f %.2f" % (trend, candle.body, fib.r61, fib.r, fib.r38, fib.e38, fib.e, fib.e61)

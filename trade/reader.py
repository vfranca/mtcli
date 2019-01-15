from .src.chart import chart_reader
from .src.bar import Bar
from .src.fib import Fib
from .src.candle_patterns import *

def get_pattern(body, top, bottom):
    """Retorna o padrão existente no candle."""
    # Verifica se é doji
    if is_doji(body, top, bottom):
        return "doji"
    # Verifica se é doji de alta
    if is_bullish_doji(body, top, bottom):
        return "doji alta"
    # Verifica se é doji dragão voador
    if is_dragon_fly_doji(body, top, bottom):
        return "doji dragão"
    # Verifica se é doji de baixa
    if is_bearish_doji(body, top, bottom):
        return "doji baixa"
    # Verifica se é doji lápide
    if is_gravestone_doji(body, top, bottom):
        return "doji lápide"
    # Verifica se é doji de quatro preços
    if is_four_prices_doji(body, top, bottom):
        return "doji de quatro preços"
    # Verifica se é marubozu
    if is_marubozu(body, top, bottom):
        return "marubozu"
    # Verifica se é spinning top
    if is_spinning_top(body, top, bottom):
        return "peão"
    # Verifica se é martelo/enforcado
    if is_hammer(body, top, bottom):
        return "martelo"
    # Verifica se é martelo invertido/estrela cadente
    if is_inverted_hammer(body, top, bottom):
        return "martelo invertido"
    return ""

def get_fib(high, low, trend):
    if trend == "alta":
        trend = "h"
    elif trend == "baixa":
        trend = "l"
    else:
        trend = "h"
    return Fib(high, low, trend)

def reader(filename, times):
    """Retorna uma lista de barras.
    
    A partir de um arquivo CSV exportado do MetaTrater 5 compõe uma lista de barras
    com abertura, máxima, mínima e fechamento
    Argumentos:
    filename: arquivo CSV MT5
    times: quantidade de barras.
    """
    rows = chart_reader(filename)
    bars = []
    for row in rows:
        bar = Bar(row)
        pattern = get_pattern(bar.body * 100, bar.top_tail * 100, bar.bottom_tail * 100)
        fib = get_fib(bar.high, bar.low, bar.trend)
        bars.append("%s %s fib %s" % (pattern, bar, fib))
        
        if len(bars) > times:
            bars.pop(0)
            
    return bars




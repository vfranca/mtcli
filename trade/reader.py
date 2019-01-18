from .src.chart import chart_reader
from .src.candle import Candle
from .src.fib import Fib
from .src.patterns import *

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
        return "doji quat pre"
    # Verifica se é marubozu
    if is_marubozu(body, top, bottom):
        return "marubozu"
    # Verifica se é spinning top
    if is_spinning_top(body, top, bottom):
        return "spin top"
    # Verifica se é martelo/enforcado
    if is_hammer(body, top, bottom):
        return "martelo"
    # Verifica se é martelo invertido/estrela cadente
    if is_inverted_hammer(body, top, bottom):
        return "martinvert"
    return ""

def get_fib(high, low, trend):
    if trend == "alta":
        trend = "h"
    elif trend == "baixa":
        trend = "l"
    else:
        trend = "h"
    return Fib(high, low, trend)

def reader(file, **kwargs):
    """Retorna uma lista de candles."""
    qtd_candles = kwargs.get("times")
    date = kwargs.get("date")
    
    chart_rows = chart_reader(file)
    candles = []
    for chart_row in chart_rows:
        candle = Candle(chart_row)
        
        # Filtra a lista de candles a partir de uma data
        if date and candle.date != date:
            continue

        pattern = get_pattern(candle.body * 100, candle.top_tail * 100, candle.bottom_tail * 100)
        fib = get_fib(candle.high, candle.low, candle.trend)
        candles.append("%s %s * %s" % (pattern, candle, fib))

        # Filtra a quantidade de candles
        if qtd_candles and len(candles) > qtd_candles:
            candles.pop(0)
            
    return candles


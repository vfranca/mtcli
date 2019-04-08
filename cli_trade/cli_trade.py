# -*- coding: utf-8 -*-
from .src.reader import *
from .src.view import *
from .src import reader, view
from .src.candle import Candle
from .src.fib import Fib
from .src.brooks_patterns2 import BrooksPatterns2

def reader(file, **kwargs):
    """Retorna uma lista de candles."""
    times = kwargs.get("times")
    date = kwargs.get("date")
    show = kwargs.get("show")
    candles = []
    high = []
    high1 = []
    low = []
    low1 = []
    body = []
    open = []
    close = []
    candle_num = 0

    rows = chart_reader(file)
    for row in rows:
        candle = Candle(row)

        # Filtra a lista de candles a partir de uma data
        if date and candle.date != date:
            continue

        # Numeração dos candles
        if date:
            candle_num += 1

        # Obtem a tendência das barras
        high.append(candle.high)
        low.append(candle.low)
        if len(high) == 2:
            trend = get_trend(high, low)
            lt_diff = get_lt_diff(high, low, trend)
            high.pop(0)
            low.pop(0)
        else:
            trend = ""
            lt_diff = 0

        # Verifica a ocorrência de padrões candlesticks de duas barras
        #body.append(candle.body)
        #open.append(candle.open)
        #close.append(candle.close)
        #if len(body) == 2:
            #pattern2 = get_two_candles_pattern(body, open, close)
            #body.pop(0)
            #open.pop(0)
            #close.pop(0)
        #else:
            #pattern2 = ""
        pattern2 = ""

        # Verifica padrões brooks de 2 barras
        body.append(candle.body)
        open.append(candle.open)
        close.append(candle.close)
        high1.append(candle.high)
        low1.append(candle.low)
        if len(body) == 2:
            brooks = BrooksPatterns2(body, open, close, high1, low1)
            bpattern2 = brooks.pattern
            body.pop(0)
            open.pop(0)
            close.pop(0)
            high1.pop(0)
            low1.pop(0)
        else:
            bpattern2 = ""

        # Seleciona a view
        if show == "full":
            candles.append(view.get_full(candle, trend, pattern2))
        elif show == "ch":
            candles.append(view.get_channel(candle, trend, lt_diff))
        elif show == "c":
            candles.append(view.get_close(candle))
        elif show == "h":
            candles.append(view.get_high(candle))
        elif show == "l":
            candles.append(view.get_low(candle))
        elif show == "r":
            candles.append(view.get_range(candle))
        elif show == "vol":
            candles.append(view.get_volume(candle, trend))
        elif show == "fib":
            candles.append(view.get_fib(candle, trend))
        elif show == "br":
            candles.append(view.get_brooks(candle, trend, candle_num, bpattern2))
        elif show == "cs":
            candles.append(view.get_default(candle, trend, pattern2))
        else:
            candles.append(view.get_brooks(candle, trend, candle_num, bpattern2))

        # Filtra a quantidade de candles
        if times and len(candles) > times:
            candles.pop(0)

    return candles


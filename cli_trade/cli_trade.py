# -*- coding: utf-8 -*-
from .src.model import bar_model
from .src import view as bar_view
from .src.helper import get_trend
from .src.candle import Candle
from .src.fib import Fib
from .src.brooks_patterns2 import BrooksPatterns2

def controller(file, **kwargs):
    """Retorna uma lista de candles."""
    times = kwargs.get("times")
    date = kwargs.get("date")
    view = kwargs.get("view")
    bars = []
    high = []
    high1 = []
    low = []
    low1 = []
    body = []
    open = []
    close = []
    num_bar = 0

    rows = bar_model(file)
    for row in rows:
        bar = Candle(row)

        # Filtra a lista de barras a partir de uma data
        if date and bar.date != date:
            continue

        # Numeração das barras
        if date:
            num_bar += 1

        # Obtem a tendência das barras
        high.append(bar.high)
        low.append(bar.low)
        if len(high) == 2:
            trend = get_trend(high, low)
            high.pop(0)
            low.pop(0)
        else:
            trend = ""

        # Verifica padrões brooks de 2 barras
        body.append(bar.body)
        open.append(bar.open)
        close.append(bar.close)
        high1.append(bar.high)
        low1.append(bar.low)
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
        if view == "full":
            bars.append(bar_view.get_full(bar, trend, pattern2))
        elif view == "ch":
            bars.append(bar_view.get_channel(bar, trend, num_bar))
        elif view == "c":
            bars.append(bar_view.get_close(bar))
        elif view == "h":
            bars.append(bar_view.get_high(bar))
        elif view == "l":
            view.append(bar_view.get_low(bar))
        elif view == "r":
            bars.append(bar_view.get_range(bar))
        elif view == "vol":
            bars.append(bar_view.get_volume(bar, trend))
        elif view == "fib":
            bars.append(bar_view.get_fib(bar, trend))
        #elif show == "br":
            #candles.append(view.get_brooks(candle, trend, num_bar, bpattern2))
        #elif show == "cs":
            #candles.append(view.get_default(candle, trend, pattern2))
        else:
            bars.append(bar_view.get_brooks(bar, trend, num_bar, bpattern2))

        # Filtra a quantidade de baras
        if times and len(bars) > times:
            bars.pop(0)

    return bars


# -*- coding: utf-8 -*-
from .src.model import bar_model
from .src import view as bar_view
from .src.helper import get_trend
from .src.candle import Candle
from .src.fib import Fib
from .src.brooks_patterns2 import BrooksPatterns2

def controller(file, **kwargs):
    """Retorna uma view."""
    qtt_bars = kwargs.get("qtt_bars")
    date = kwargs.get("date")
    view = kwargs.get("view")
    views = []
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

        # Filtra a lista de views a partir de uma data
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

        # Seleção da view
        if view == "full":
            views.append(bar_view.get_full(bar, trend, pattern2))
        elif view == "ch":
            views.append(bar_view.get_channel(bar, trend, num_bar))
        elif view == "c":
            views.append(bar_view.get_close(bar))
        elif view == "h":
            views.append(bar_view.get_high(bar))
        elif view == "l":
            views.append(bar_view.get_low(bar))
        elif view == "r":
            views.append(bar_view.get_range(bar))
        elif view == "vol":
            views.append(bar_view.get_volume(bar, trend))
        elif view == "fib":
            views.append(bar_view.get_fib(bar, trend))
        else:
            views.append(bar_view.get_brooks(bar, trend, num_bar, bpattern2))

        # Filtra a quantidade de views
        if qtt_bars and len(views) > qtt_bars:
            views.pop(0)

    return views


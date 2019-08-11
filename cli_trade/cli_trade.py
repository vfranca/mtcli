# -*- coding: utf-8 -*-
from cli_trade.model import bar_model
from cli_trade.view import *
from cli_trade.helper import get_fib
from cli_trade.candle import Candle
from cli_trade.fib import Fib
from cli_trade.brooks_patterns1 import BrooksPatterns1
from cli_trade.brooks_patterns2 import BrooksPatterns2
from cli_trade.settings import *


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
    count = bull = bear = doji =0

    bars = bar_model(file)
    for item in bars:
        bar = Candle(item)
        count += 1

        # Filtra a lista de views a partir de uma data
        if date and bar.date != date:
            continue

        # Numeração das barras
        if date:
            num_bar += 1

        # Verifica padrões brooks de 2 barras
        body.append(bar.body)
        open.append(bar.open)
        close.append(bar.close)
        high1.append(bar.high)
        low1.append(bar.low)
        if len(body) == 2:
            brooks = BrooksPatterns2(body, open, close, high1, low1)
            pattern2 = brooks.pattern
            trend = brooks.trend
            body.pop(0)
            open.pop(0)
            close.pop(0)
            high1.pop(0)
            low1.pop(0)
        else:
            pattern2 = ""
            trend = ""

        # Contagem de barras de tendência e barras doji
        if qtt_bars:
            start = len(bars) - qtt_bars
            if count > start:
                fib = get_fib(bar.high, bar.low, bar.trend)
                pattern1 = BrooksPatterns1(bar.body, bar.top, bar.bottom, bar.close, fib.r)
                if pattern1.pattern == lbl_buy_pressure:
                    bull += 1
                elif pattern1.pattern == lbl_sell_pressure:
                    bear += 1
                else:
                    doji += 1

        # Seleção da view
        if view == "full":
            views.append(full_view(bar, trend, pattern2))
        elif view == "ch":
            views.append(channel_view(bar, trend, num_bar))
        elif view == "c":
            views.append(close_view(bar))
        elif view == "h":
            views.append(high_view(bar))
        elif view == "l":
            views.append(low_view(bar))
        elif view == "r":
            views.append(range_view(bar))
        elif view == "vol":
            views.append(volume_view(bar, trend))
        elif view == "fib":
            views.append(fib_view(bar, trend))
        elif view == "stat":
            views = [stat_view(bull, bear, doji)]
        else:
            views.append(brooks_view(bar, trend, num_bar, pattern2))

        # Limita a quantidade de views
        if qtt_bars and len(views) > qtt_bars:
            views.pop(0)

    return views


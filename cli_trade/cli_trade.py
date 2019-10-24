# -*- coding: utf-8 -*-
from cli_trade._model import bar_model
from cli_trade import _view
from cli_trade import _helper
from cli_trade.lib.bar import Bar
from cli_trade.lib.brooks_patterns1 import BrooksPatterns1
from cli_trade.lib.brooks_patterns2 import BrooksPatterns2
from cli_trade.conf import *


def controller(file, **kwargs):
    """Retorna uma view."""
    qtt_bars = kwargs.get("qtt_bars")
    date = kwargs.get("date")
    view = kwargs.get("view")
    views = close = open = high = low = high1 = low1 = body = []
    num_bar = count = bull = bear = doji = 0

    bars = bar_model(file)
    for item in bars:
        bar = Bar(item)
        count += 1

        # Filtra a lista de views a partir de uma data
        if date and bar.date != date:
            continue

        # Obtem o número da barra
        if date:
            num_bar += 1
        else:
            num_bar = ""

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
                mp = _helper.get_medium_point(bar)
                pattern1 = BrooksPatterns1(bar.body, bar.top, bar.bottom, bar.close, mp)
                if pattern1.pattern == conf.lbl_buy_pressure:
                    bull += 1
                elif pattern1.pattern == conf.lbl_sell_pressure:
                    bear += 1
                else:
                    doji += 1

        # Seleção da view
        if view == "ohlc":
            views.append(_view.ohlc_view(bar))
        elif view == "ch":
            views.append(_view.channel_view(bar, trend, num_bar))
        elif view == "c":
            views.append(_view.close_view(bar, num_bar))
        elif view == "h":
            views.append(_view.high_view(bar, num_bar))
        elif view == "l":
            views.append(_view.low_view(bar, num_bar))
        elif view == "r":
            views.append(_view.range_view(bar, trend, num_bar))
        elif view == "vol":
            views.append(_view.volume_view(bar, trend, num_bar))
        elif view == "stat":
            views = [stat_view(bull, bear, doji)]
        else:
            views.append(_view.brooks_view(bar, trend, num_bar, pattern2))

        # Limita a quantidade de views
        if qtt_bars and len(views) > qtt_bars:
            views.pop(0)

    return views

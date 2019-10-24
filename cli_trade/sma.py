# -*- coding: utf-8 -*-
from cli_trade._model import bar_model
from cli_trade.lib.bar import Bar
from cli_trade import conf


def ma(bars_qtt, file):
    """ Calcula a média móvel simples dos preços de fechamento."""
    prices = []
    rows = bar_model(file)
    for row in rows:
        bar = Bar(row)
        prices.append(bar.close)
    prices = prices[-bars_qtt:]
    return round(sum(prices) / len(prices), conf.digits)

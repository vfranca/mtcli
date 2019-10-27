# -*- coding: utf-8 -*-
from cli_trade._model import bar_model
from cli_trade.lib.bar import Bar
from cli_trade import conf


def get_sma(symbol, period, count=20):
    """ Calcula a média móvel simples dos preços de fechamento."""
    file = conf.csv_path + symbol + period + ".csv"
    prices = []
    rows = bar_model(file)
    for row in rows:
        bar = Bar(row)
        prices.append(bar.close)
    prices = prices[-count:]
    return round(sum(prices) / len(prices), conf.digits)

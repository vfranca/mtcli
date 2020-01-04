# -*- coding: utf-8 -*-
from mtcli.model import bar_model
from mtcli.bar import Bar
from mtcli import conf


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

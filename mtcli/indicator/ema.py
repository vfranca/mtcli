# -*- coding: utf-8 -*-
from mtcli.model import bar_model
from mtcli.bar import Bar
from mtcli import conf


def get_k(count=20):
    """ Calcula o coeficiente multiplicador."""
    return round(2 / (count + 1), 3)


def get_price_close(file):
    """ Obtem o preço de fechamento atual."""
    rows = bar_model(file)
    for row in rows:
        bar = Bar(row)
        price_close = bar.close
    return price_close


def get_last_ema(file, count=20):
    """ Obtem a última EMA. """
    prices = []
    rows = bar_model(file)
    for row in rows:
        bar = Bar(row)
        prices.append(bar.close)
    prices = prices[-(count + 1) : -1]
    return round(sum(prices) / len(prices), 2)


def get_ema(symbol, period, count=20):
    """ Calcula a média móvel exponencial dos preços de fechamento."""
    file = conf.csv_path + symbol + period + ".csv"
    k = get_k(count)
    close = get_price_close(file)
    last_ema = get_last_ema(file, count)
    return round(close * k + last_ema * (1 - k), conf.digits)

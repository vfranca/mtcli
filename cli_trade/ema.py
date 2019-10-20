# -*- coding: utf-8 -*-
from cli_trade._model import bar_model
from cli_trade._bar import Bar
from cli_trade.conf import *


def get_k(bars_qtt):
    """ Calcula o coeficiente multiplicador."""
    return round(2 / (bars_qtt + 1), 3)

def get_price_close(filename):
    """ Obtem o preço de fechamento atual."""
    rows = bar_model(filename)
    for row in rows:
        bar = Bar(row)
        price_close = bar.close
    return price_close

def get_last_ema(bars_qtt, filename):
    """ Obtem a última EMA. """
    prices = []
    rows = bar_model(filename)
    for row in rows:
        bar = Bar(row)
        prices.append(bar.close)
    prices = prices[-(bars_qtt+1):-1]
    return round(sum(prices) / len(prices), 2)

def get_ema(bars_qtt, filename):
    """ Calcula a média móvel exponencial dos preços de fechamento.

    Extrai os preços de fechamento de um arquivo CSV exportado do MetaTrater 5
    em um dado período
    Argumentos:
    k: coeficiente multiplicador
    last_ema: última EMA
    close: preço de fechamento.
    """
    k = get_k(bars_qtt)
    close = get_price_close(filename)
    last_ema = get_last_ema(bars_qtt, filename)
    return round(close * k + last_ema * (1 - k), digits)

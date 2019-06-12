from .src.model import bar_model
from .src.candle import Candle
from .settings import *


def get_k(times):
    """ Calcula o coeficiente multiplicador."""
    return round(2 / (times + 1), 3)

def get_price_close(filename):
    """ Obtem o preço de fechamento atual."""
    rows = bar_model(filename)
    for row in rows:
        candle = Candle(row)
        price_close = candle.close
    return price_close

def get_last_ema(times, filename):
    """ Obtem a última EMA. """
    prices = []
    rows = bar_model(filename)
    for row in rows:
        candle = Candle(row)
        prices.append(candle.close)
    prices = prices[-(times+1):-1]
    return round(sum(prices) / len(prices), 2)

def get_ema(times, filename):
    """ Calcula a média móvel exponencial dos preços de fechamento.

    Extrai os preços de fechamento de um arquivo CSV exportado do MetaTrater 5
    em um dado período
    Argumentos:
    k: coeficiente multiplicador
    last_ema: última EMA
    close: preço de fechamento.
    """
    k = get_k(times)
    close = get_price_close(filename)
    last_ema = get_last_ema(times, filename)
    return round(close * k + last_ema * (1 - k), digits)

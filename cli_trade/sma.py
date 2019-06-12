from.src.model import bar_model
from .src.candle import Candle
from .settings import *


def ma(candles, file):
    """ Calcula a média móvel simples dos preços de fechamento."""
    prices = []
    rows = bar_model(file)
    for row in rows:
        candle = Candle(row)
        prices.append(candle.close)
    prices = prices[-candles:]
    return round(sum(prices) / len(prices), digits)

# -*- coding: utf-8 -*-
from cli_trade.model import bar_model
from cli_trade.candle import Candle
from cli_trade.settings import *


def ma(candles, file):
    """ Calcula a média móvel simples dos preços de fechamento."""
    prices = []
    rows = bar_model(file)
    for row in rows:
        candle = Candle(row)
        prices.append(candle.close)
    prices = prices[-candles:]
    return round(sum(prices) / len(prices), digits)

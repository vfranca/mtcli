"""
Simple Moving Average ou SMA
"""
from mtcli.models import BarModel
from mtcli.bar import Bar
from mtcli import conf


def get_sma(symbol, period, count=20):
    """ Calcula a média móvel simples dos preços de fechamento."""
    csv_file = conf.csv_path + symbol + period + ".csv"
    prices = []
    bars = BarModel(csv_file)
    for item in bars:
        bar = Bar(item)
        prices.append(bar.close)
    prices = prices[-count:]
    return round(sum(prices) / len(prices), conf.digits)

"""
Simple Moving Average ou SMA
"""
from mtcli.csv_data import Rates
from mtcli.pa.pa_bar import Bar
from mtcli import conf


def get_sma(symbol, period, count=20):
    """Calcula a média móvel simples dos preços de fechamento."""
    csv_file = conf.csv_path + symbol + period + ".csv"
    prices = []
    rates = Rates(csv_file)
    for rate in rates:
        bar = Bar(rate)
        prices.append(bar.close)
    prices = prices[-count:]
    return round(sum(prices) / len(prices), conf.digits)

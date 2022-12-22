"""
Exponential Moving Average ou EMA
"""
from mtcli.csv_data import Rates
from mtcli.pa.pa_bar import Bar
from mtcli import conf


def get_k(count=20):
    """Calcula o coeficiente multiplicador."""
    return round(2 / (count + 1), 3)


def get_price_close(csv_file):
    """Obtem o preço de fechamento atual."""
    bars = BarModel(csv_file)
    price_close = 0.0
    for item in bars:
        bar = Bar(item)
        price_close = bar.close
    return price_close


def get_last_ema(csv_file, count=20):
    """Obtem a última EMA."""
    prices = []
    bars = BarModel(csv_file)
    for item in bars:
        bar = Bar(item)
        prices.append(bar.close)
    prices = prices[-(count + 1) : -1]
    return round(sum(prices) / len(prices), 2)


def get_ema(symbol, period, count=20):
    """Calcula a média móvel exponencial dos preços de fechamento."""
    csv_file = conf.csv_path + symbol + period + ".csv"
    k = get_k(count)
    close = get_price_close(csv_file)
    last_ema = get_last_ema(csv_file, count)
    return round(close * k + last_ema * (1 - k), conf.digits)

"""
Average True Range ou ATR
"""
from mtcli.csv_data import Rates
from mtcli.pa.pa_bar import Bar
from mtcli import conf


def get_atr(symbol, period, count):
    """Calcula o ATR."""
    csv_file = conf.csv_path + symbol + period + ".csv"
    ranges = []
    rates = Rates(csv_file)
    for rate in rates:
        bar = Bar(rate)
        # Elimina doji de 4 preços
        if bar.open == bar.high and bar.high == bar.low and bar.low == bar.close:
            continue
        ranges.append(bar.high - bar.low)
    ranges = ranges[-count:]
    return round(sum(ranges) / len(ranges), conf.digits)

"""
Average True Range ou ATR
"""
from mtcli.models import BarModel
from mtcli.bar import Bar
from mtcli import conf


def get_atr(symbol, period, count):
    """Calcula o ATR."""
    csv_file = conf.csv_path + symbol + period + ".csv"
    ranges = []
    bars = BarModel(csv_file)
    for item in bars:
        bar = Bar(item)
        # Elimina doji de 4 preços
        if bar.open == bar.high and bar.high == bar.low and bar.low == bar.close:
            continue
        ranges.append(bar.high - bar.low)
    ranges = ranges[-count:]
    return round(sum(ranges) / len(ranges), conf.digits)

# -*- coding: utf-8 -*-
from cli_trade._model import bar_model
from cli_trade.lib.bar import Bar
from cli_trade import conf


def get_atr(symbol, period, count):
    """Calcula o ATR."""
    file = conf.csv_path + symbol + period + ".csv"
    ranges = []
    rows = bar_model(file)
    for row in rows:
        bar = Bar(row)
        # Elimina doji de 4 preços
        if bar.open == bar.high and bar.high == bar.low and bar.low == bar.close:
            continue
        ranges.append(bar.high - bar.low)
    ranges = ranges[-count:]
    return round(sum(ranges) / len(ranges), conf.digits)

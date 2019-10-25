# -*- coding: utf-8 -*-
from cli_trade._model import bar_model
from cli_trade.lib.bar import Bar


def atr(file, bars):
    """Calcula o ATR."""
    ranges = []
    rows = bar_model(file)
    for row in rows:
        bar = Bar(row)
        # Elimina doji de 4 precos
        if bar.open == bar.high and bar.high == bar.low and bar.low == bar.close:
            continue
        ranges.append(bar.high - bar.low)
    ranges = ranges[-bars:]
    return round(sum(ranges) / len(ranges), 2)


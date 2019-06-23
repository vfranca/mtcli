# -*- coding: utf-8 -*-
from.src.model import bar_model
from .src.candle import Candle


def atr(file, candles):
    """Calcula o ATR."""
    ranges = []
    rows = bar_model(file)
    for row in rows:
        candle = Candle(row)
        # Elimina doji de 4 precos
        if candle.open == candle.high and candle.high == candle.low and candle.low == candle.close:
            continue
        ranges.append(candle.high - candle.low)
    ranges = ranges[-candles:]
    return round(sum(ranges) / len(ranges), 2)


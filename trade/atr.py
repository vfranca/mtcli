from.src.reader import chart_reader
from .src.candle import Candle

def atr(file, candles):
    """Calcula o ATR."""
    ranges = []
    rows = chart_reader(file)
    for row in rows:
        candle = Candle(row)
        ranges.append(candle.high - candle.low)
    ranges = ranges[-candles:]
    return sum(ranges) / len(ranges)

    
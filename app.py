#!/usr/bin/python3
import sys
from trade.candle import Candle
from templates import ohlc

str_ohlc = sys.argv[1]

candle = Candle(str_ohlc)
print(ohlc.tmpl % candle.open, candle.max, candle.min, candle.close)

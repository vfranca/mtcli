from trade import chart_reader, Candle
import sys

filename = "var/" + sys.argv[1]
candles = chart_reader(filename)
for row in candles:
    c = Candle(row)
    print(c.high_trend_low())

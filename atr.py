from trade.atr import atr
import sys

file = "var/%s.csv" % sys.argv[1]
if len(sys.argv) == 3:
    candles = int(sys.argv[2])
else:
    candles = 14
atr = atr(file, candles)
print(atr)


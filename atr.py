from cli_trade.atr import atr
from cli_trade.settings import *
import sys

file = "%s%s.csv" % (csv_path, sys.argv[1])

if len(sys.argv) == 3:
    candles = int(sys.argv[2])
else:
    candles = 14
atr = atr(file, candles)
print(atr)


from trade.atr import atr
import sys

file = "C:/Users/Administrador/AppData/Roaming/MetaQuotes/Terminal/FB9A56D617EDDDFE29EE54EBEFFE96C1/MQL5/Files/%s.csv" % sys.argv[1]
if len(sys.argv) == 3:
    candles = int(sys.argv[2])
else:
    candles = 14
atr = atr(file, candles)
print(atr)


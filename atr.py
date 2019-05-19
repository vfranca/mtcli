from cli_trade.atr import atr
import sys

file = "C:/Users/Administrador/AppData/Roaming/MetaQuotes/Terminal/FB9A56D617EDDDFE29EE54EBEFFE96C1/MQL5/Files/%s.csv" % sys.argv[1]
#file = "C:/Users/Administrador/AppData/Roaming/MetaQuotes/Terminal/83D4764E0403A8685E84D6FCAB361879/MQL5/Files/%s.csv" % sys.argv[1]

if len(sys.argv) == 3:
    candles = int(sys.argv[2])
else:
    candles = 14
atr = atr(file, candles)
print(atr)


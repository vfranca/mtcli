from cli_trade.sma import ma
import sys

times = int(sys.argv[1])
filename = "C:/Users/Administrador/AppData/Roaming/MetaQuotes/Terminal/FB9A56D617EDDDFE29EE54EBEFFE96C1/MQL5/Files/" + sys.argv[2]
#filename = "C:/Users/Administrador/AppData/Roaming/MetaQuotes/Terminal/83D4764E0403A8685E84D6FCAB361879/MQL5/Files/" + sys.argv[2]

mms = ma(times, filename)
print(mms)


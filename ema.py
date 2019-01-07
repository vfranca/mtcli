from trade.ema import get_ema
import sys

times = int(sys.argv[1])
filename = "var/" + sys.argv[2]
mm = get_ema(times, filename)
print(mm)


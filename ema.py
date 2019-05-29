from cli_trade.ema import get_ema
from cli_trade.settings import *
import sys

times = int(sys.argv[1])
filename = csv_path + sys.argv[2]

mm = get_ema(times, filename)
print(mm)


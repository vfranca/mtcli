from trade import chart_reader, Bar, ma
import sys

times = int(sys.argv[1])
filename = "var/" + sys.argv[2]
mms = ma(times, filename)
print(mms)


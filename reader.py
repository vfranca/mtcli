from trade.reader import reader
import sys

filename = "var/" + sys.argv[1]
times = int(sys.argv[2])

bars = reader(filename, times)
for bar in bars:
    print(bar)

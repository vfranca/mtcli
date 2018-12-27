from trade import reader
import sys

filename = "var/" + sys.argv[1]
times = 10
bars = reader(filename, times)
for bar in bars:
    print(bar)

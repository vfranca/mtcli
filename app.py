from trade import chart_reader, Bar
import sys

filename = "var/" + sys.argv[1]
rows = chart_reader(filename)
c = 0
for row in rows:
    bar = Bar(row)
    print(bar.high_trend_low())

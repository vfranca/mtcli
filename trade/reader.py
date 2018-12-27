from .chart import chart_reader
from .bar import Bar

def reader(filename, times):
    rows = chart_reader(filename)
    bars = []
    for row in rows:
        bar = Bar(row)
        bars.append(bar)
        if len(bars) > times:
            bars.pop(0)
    return bars




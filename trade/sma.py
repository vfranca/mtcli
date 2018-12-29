from .chart import chart_reader
from .bar import Bar

def ma(times, filename):
    rows = chart_reader(filename)
    prices = []

    for row in rows:
        bar = Bar(row)
        prices.append(bar.close)
        if len(prices) > times:
            prices.pop(0)
    return round(sum(prices) / times)

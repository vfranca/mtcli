from.src.chart import chart_reader
from .src.candle import Candle

def ma(times, filename):
    """ Calcula a média móvel simples dos preços de fechamento
    
    Extrai os preços de fechamento de um arquivo CSV exportado do MetaTrater 5
    em um dado período 
    Argumentos:
    times: número de períodos
    filename: arquivo CSV do MT5."""
    rows = chart_reader(filename)
    prices = []
    for row in rows:
        bar = Candle(row)
        prices.append(bar.close)
        if len(prices) > times:
            prices.pop(0)
    return round(sum(prices) / times)

from .src.chart import chart_reader
from .src.bar import Bar
from .src.fib import Fib

def reader(filename, times):
    """Retorna uma lista de barras.
    
    A partir de um arquivo CSV exportado do MetaTrater 5 compõe uma lista de barras
    com abertura, máxima, mínima e fechamento
    Argumentos:
    filename: arquivo CSV MT5
    times: quantidade de barras.
    """
    rows = chart_reader(filename)
    bars = []
    for row in rows:
        bar = Bar(row)
        if bar.trend == "alta":
            trend = "h"
        elif bar.trend == "baixa":
            trend = "l"
        else:
            trend = "h"
        fib = Fib(bar.high, bar.low, trend)
        bars.append(str(bar) + " fibo " + str(fib))
        if len(bars) > times:
            bars.pop(0)
    return bars




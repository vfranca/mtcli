from .src.chart import chart_reader
from .src.bar import Bar

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
        bars.append(bar)
        if len(bars) > times:
            bars.pop(0)
    return bars




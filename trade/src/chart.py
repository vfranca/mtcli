import csv

def chart_reader(filename):
    """ Lê um gráfico de barras/candlestick para uma lista.
    
    Lê um arquivo CSV exportado do MetaTrader 5
    Retorna uma lista de listas.
    Argumentos:
    filename: arquivo CSV MT5.
    """
    f = open(filename, encoding = "utf-16", newline = "")
    r = csv.reader(f, delimiter = ',', quotechar = '\'')
    return r

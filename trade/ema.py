from .chart import chart_reader
from .bar import Bar

def get_k(times):
    """ Calcula o coeficiente multiplicador."""
    return round(2 / (times + 1), 3)

def get_close(filename):
    """ Obtem o preço de fechamento atual."""
    pass

def get_last_ema(times, filename):
    """ Obtem a última EMA. """
    pass

def get_ema(k, last_ema, close):
    """ Calcula a média móvel exponencial dos preços de fechamento.
    
    Extrai os preços de fechamento de um arquivo CSV exportado do MetaTrater 5
    em um dado período 
    Argumentos:
    k: coeficiente multiplicador
    last_ema: última EMA
    close: preço de fechamento.
    """
    return close * k + last_ema * (1 - k)

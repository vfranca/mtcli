from .src.chart import chart_reader
from .src.candle import Candle

def get_k(times):
    """ Calcula o coeficiente multiplicador."""
    return round(2 / (times + 1), 3)

def get_price_close(filename):
    """ Obtem o preço de fechamento atual."""
    rows = chart_reader(filename)
    for row in rows:
        bar = Candle(row)
        price_close = bar.close
    return price_close

def get_last_ema(times, filename):
    """ Obtem a última EMA. """
    rows = chart_reader(filename)
    prices = []
    for row in rows:
        bar = Candle(row)
        prices.append(bar.close)
        if len(prices) > (times + 1):
            prices.pop(0)
    prices.pop(len(prices) - 1)
    return round(sum(prices) / times)

def get_ema(times, filename):
    """ Calcula a média móvel exponencial dos preços de fechamento.
    
    Extrai os preços de fechamento de um arquivo CSV exportado do MetaTrater 5
    em um dado período 
    Argumentos:
    k: coeficiente multiplicador
    last_ema: última EMA
    close: preço de fechamento.
    """
    k = get_k(times)
    close = get_price_close(filename)
    last_ema = get_last_ema(times, filename)
    return round(close * k + last_ema * (1 - k))

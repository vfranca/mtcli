from .src.reader import *
from .src.candle import Candle
from .src.fib import Fib

def reader(file, **kwargs):
    """Retorna uma lista de candles."""
    qtd_candles = kwargs.get("times")
    date = kwargs.get("date")
    
    chart_rows = chart_reader(file)
    candles = []
    highs = []
    lows = []
    body = []
    open = []
    close = []
    
    for chart_row in chart_rows:
        candle = Candle(chart_row)
        
        # Filtra a lista de candles a partir de uma data
        if date and candle.date != date:
            continue
        
        # Obtem a tendencia de topos e fundos
        highs.append(candle.high)
        lows.append(candle.low)
        if len(highs) == 2:
            trend = get_trend(highs, lows)
            highs.pop(0)
            lows.pop(0)
        else:
            trend = ""

        # Verifica padrões complexos
        body.append(candle.body)
        open.append(candle.open)
        close.append(candle.close)
        if len(body) == 2:
            complex_pattern = get_two_candles_pattern(body, open, close)
            body.pop(0)
            open.pop(0)
            close.pop(0)
        else:
            complex_pattern = ""

        candles.append(get_show_default(candle, trend = trend, complex_pattern = complex_pattern))

        # Filtra a quantidade de candles
        if qtd_candles and len(candles) > qtd_candles:
            candles.pop(0)
            
    return candles

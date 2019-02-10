from .src.reader import *
from .src.candle import Candle
from .src.fib import Fib

def reader(file, **kwargs):
    """Retorna uma lista de candles."""
    times = kwargs.get("times")
    date = kwargs.get("date")
    show = kwargs.get("show")
    candles = []
    high = []
    low = []
    body = []
    open = []
    close = []
    
    rows = chart_reader(file)
    for row in rows:
        candle = Candle(row)
        # Filtra a lista de candles a partir de uma data
        if date and candle.date != date:
            continue
        # Obtem a tendencia de topos e fundos
        high.append(candle.high)
        low.append(candle.low)
        if len(high) == 2:
            trend = get_trend(high, low)
            lt_diff = get_lt_diff(high, low, trend)
            high.pop(0)
            low.pop(0)
        else:
            trend = ""
            lt_diff = 0
        # Verifica a ocorrência de padr?es de dois candles
        body.append(candle.body)
        open.append(candle.open)
        close.append(candle.close)
        if len(body) == 2:
            pattern2 = get_two_candles_pattern(body, open, close)
            body.pop(0)
            open.pop(0)
            close.pop(0)
        else:
            pattern2 = ""

        # Seleciona a exibição
        if show == "full":
            candles.append(get_show_full(candle, trend, pattern2))
        elif show == "channel":
            candles.append(get_show_channel(candle, trend, lt_diff))
        elif show == "close":
            candles.append(get_show_close(candle))
        elif show == "vol":
            candles.append(get_show_volume(candle, trend))
        elif show == "brooks":
            candles.append(get_show_brooks(candle, trend))
        elif show == "wdo":
            candles.append(get_show_wdo(candle, trend, pattern2))
        elif show == "stock":
            candles.append(get_show_stock(candle, trend, pattern2))
        else:
            candles.append(get_show_default(candle, trend, pattern2))

        # Filtra a quantidade de candles
        if times and len(candles) > times:
            candles.pop(0)
            
    return candles

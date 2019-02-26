from .src.reader import *
from .src.view import *
from .src import reader, view
from .src.candle import Candle
from .src.fib import Fib
from .src.brooks_patterns import *

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
    candle_num = 0
    
    rows = chart_reader(file)
    for row in rows:
        candle = Candle(row)

        # Filtra a lista de candles a partir de uma data
        if date and candle.date != date:
            continue

        # Numeração dos candles
        if date:
            candle_num += 1

        # Obtem a tendencia de canal
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

        # Verifica a ocorrência de padrões candlesticks de dois candles
        if show == "candles":
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

        # Verifica padrões brooks de 2 barras
        body.append(candle.body)
        open.append(candle.open)
        close.append(candle.close)
        if len(body) == 2:
            pattern_bars = get_pattern_bars(body, open, close)
            body.pop(0)
            open.pop(0)
            close.pop(0)
        else:
            pattern_bars = ""

        # Seleciona a view
        if show == "full":
            candles.append(view.get_full(candle, trend, pattern_bars))
        elif show == "channel":
            candles.append(view.get_channel(candle, trend, lt_diff))
        elif show == "close":
            candles.append(view.get_close(candle))
        elif show == "high":
            candles.append(view.get_high(candle))
        elif show == "low":
            candles.append(view.get_low(candle))
        elif show == "range":
            candles.append(view.get_range(candle))
        elif show == "vol":
            candles.append(view.get_volume(candle, trend))
        elif show == "fib":
            candles.append(view.get_fib(candle, trend))
        elif show == "brooks":
            candles.append(view.get_brooks(candle, trend, candle_num, pattern_bars))
        elif show == "candles":
            candles.append(view.get_default(candle, trend, pattern2))
        else:
            candles.append(view.get_brooks(candle, trend, candle_num, pattern_bars))

        # Filtra a quantidade de candles
        if times and len(candles) > times:
            candles.pop(0)
            
    return candles

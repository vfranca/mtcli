from .patterns import *
from .brooks_patterns1 import BrooksPatterns1
from . import reader
from trade.settings import *

def get_default(c, trend, pattern2):
    """Retorna a exibição no formato padrão."""
    f = reader.get_fib(c.high, c.low, c.trend)
    p = get_pattern(c.body, c.top, c.bottom)
    view = "%s %s %s %i"
    view += " %s %s %s * %s %s" % (r, r, r, r, r)
    return view % (trend, pattern2, p, c.body, c.high, c.low, c.close, f.r, f.e)

def get_full(c, trend, pattern2):
    """Retorna a exibição no formato completo."""
    p = get_pattern(c.body, c.top, c.bottom)
    f = reader.get_fib(c.high, c.low, c.trend)
    view = "%s %s %s %i"
    view += " %s %s %s %s * %s %s" % (r, r, r, r, r, r)
    return view % (trend, pattern2, p, c.body, c.open, c.high, c.low, c.close, f.r, f.e)

def get_channel(c, trend, lt_diff):
    """Retorna a exibição no formato de canal."""
    lt_high = c.high + lt_diff
    lt_low = c.low + lt_diff
    view = "%s"
    view += " %s %s * %s %s" % (r, r, r, r)
    return view % (trend, c.high, c.low, lt_high, lt_low)

def get_lt_diff(high, low, trend):
    if trend == "asc":
        return low[1] - low[0]
    elif trend == "desc":
        return high[1] - high[0]
    else:
        return 0

def get_close(c):
    """Retorna a exibição com os fechamentos."""
    view = ""
    view += "%s" % r
    return view % c.close

def get_high(c):
    """Retorna a exibição com as máximas."""
    view = ""
    view += "%s" % r
    return view % c.high

def get_low(c):
    """Retorna a exibição com as mínimas."""
    view = ""
    view += "%s" % r
    return view % c.low

def get_volume(c, trend):
    """Retorna a exibição com os volumes."""
    view = "%s"
    view += " %s" % r
    return view % (trend, c.volume)

def get_range(c):
    """Retorna a view com os ranges das barras."""
    return "%i" % c.range

def get_brooks(c, trend, num, pattern2):
    """Retorna a exibição com os padrões de Brooks."""
    f = reader.get_fib(c.high, c.low, c.trend) # Números de Fibonacci
    b = BrooksPatterns1(c.body, c.top, c.bottom, c.close, f.r) # padrões de 1 barra
    
    tail = b.tail
    if tail == "TOPTAIL":
        tail = "%s%i" %(tail, c.top)
    if tail == "BOTTOMTAIL":
        tail = "%s%i" %(tail, c.bottom)
    
    num =str(num)
    if num == "0":
        num = ""
        
    view = "%s %s %s %s%iR%i %s %s"
    view += " %s %s %s * %s %s" % (r, r, r, r, r)
    return view % (num, trend, b.pattern, b.body_pattern, abs(c.body), c.body_range, pattern2, tail, c.high, c.low, c.close, f.r, f.e)

def get_fib(c, trend):
    """Retorna a exibição de Fibonacci."""
    f = reader.get_fib(c.high, c.low, c.trend)
    view = "%s %i"
    view += " %s %s %s * %s %s %s" % (r, r, r, r, r, r)
    return view % (trend, c.body, f.r61, f.r, f.r38, f.e38, f.e, f.e61)

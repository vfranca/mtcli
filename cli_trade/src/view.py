from .patterns import *
from .brooks_patterns1 import BrooksPatterns1
from . import helper
from cli_trade.settings import *

def full_view(c, trend, pattern2):
    """Retorna a exibição no formato completo."""
    p = get_pattern(c.body, c.top, c.bottom)
    f = helper.get_fib(c.high, c.low, c.trend)
    view = "%s %s %s %i"
    view += " %s %s %s %s * %s %s" % (r, r, r, r, r, r)
    return view % (trend, pattern2, p, c.body, c.open, c.high, c.low, c.close, f.r, f.e)

def channel_view(c, trend, num):
    """Retorna a exibição no formato de canal."""
    view = "%s"
    view += " %s %s" % (r, r)
    view += " %s"
    return view % (trend, c.high, c.low, num)

def close_view(c):
    """Retorna a exibição com os fechamentos."""
    view = ""
    view += "%s" % r
    return view % c.close

def high_view(c):
    """Retorna a exibição com as máximas."""
    view = ""
    view += "%s" % r
    return view % c.high

def low_view(c):
    """Retorna a exibição com as mínimas."""
    view = ""
    view += "%s" % r
    return view % c.low

def volume_view(c, trend):
    """Retorna a exibição com os volumes."""
    view = "%s"
    view += " %s" % r
    return view % (trend, c.volume)

def range_view(c):
    """Retorna a view com os ranges das barras."""
    return "%i" % c.range

def brooks_view(c, trend, num, pattern2):
    """Retorna a exibição com os padrões de Brooks."""
    f = helper.get_fib(c.high, c.low, c.trend) # Números de Fibonacci
    b = BrooksPatterns1(c.body, c.top, c.bottom, c.close, f.r) # padrões de 1 barra

    tail = b.tail
    if tail == lbl_toptail:
        tail = "%s%i" %(tail, c.top)
    if tail == lbl_bottomtail:
        tail = "%s%i" %(tail, c.bottom)

    num =str(num)
    if num == "0":
        num = ""

    view = "%s %s %s %s%iR%i %s %s"
    view += " %s %s %s * %s %s" % (r, r, r, r, r)
    return view % (num, trend, b.pattern, b.body_pattern, abs(c.body), c.body_range, pattern2, tail, c.high, c.low, c.close, f.r, f.e)

def fib_view(c, trend):
    """Retorna a exibição de Fibonacci."""
    f = helper.get_fib(c.high, c.low, c.trend)
    view = "%s %i"
    view += " %s %s %s * %s %s %s" % (r, r, r, r, r, r)
    return view % (trend, c.body, f.r61, f.r, f.r38, f.e38, f.e, f.e61)

def stat_view(bull, bear, doji):
    """ Retorna a view stat."""
    return "verde %i vermelho %i doji %i" % (bull, bear, doji)

# -*- coding: utf-8 -*-
from cli_trade._patterns import *
from cli_trade._brooks_patterns1 import BrooksPatterns1
from cli_trade import _helper
from cli_trade.conf import *


def brooks_view(bar, ch_trend, num_bar, brooks_pattern2):
    """Retorna a exibição com os padrões Brooks."""
    medium_point = bar.range / 2
    brooks1 = BrooksPatterns1(bar.body, bar.top, bar.bottom, bar.close, medium_point) # padrões de 1 barra

    tail = brooks1.tail
    if tail == lbl_toptail:
        tail = "%s%i" %(tail, bar.top)
    if tail == lbl_bottomtail:
        tail = "%s%i" %(tail, bar.bottom)

    view = "%s %s %s %s%iR%." + str(digits) + "f %s %s"
    view += " %s %s %s" % (r, r, r)
    view += " R%.2f"

    return view % (num_bar, ch_trend, brooks1.pattern, brooks1.body_pattern, abs(bar.body), bar.body_range, brooks_pattern2, tail, bar.high, bar.low, bar.close, bar.range)

def full_view(c, trend, pattern2):
    """Retorna a exibição no formato completo."""
    f = _helper.get_fib(c.high, c.low, c.trend)
    view = "%s %s %i"
    view += " %s %s %s %s * %s %s" % (r, r, r, r, r, r)
    return view % (trend, pattern2, c.body, c.open, c.high, c.low, c.close, f.r, f.e)

def channel_view(bar, ch_trend, num_bar):
    """Retorna a exibição no formato de canal."""
    view = "%s %s"
    view += " %s %s" % (r, r)

    return view % (num_bar, ch_trend, bar.high, bar.low)

def close_view(bar, num_bar):
    """Retorna a exibição com os fechamentos."""
    view = "%s "
    view += "%s" % r

    return view % (num_bar, bar.close)

def high_view(bar, num_bar):
    """Retorna a exibição com as máximas."""
    view = "%s "
    view += "%s" % r

    return view % (num_bar, bar.high)

def low_view(bar, num_bar):
    """Retorna a exibição com as mínimas."""
    view = "%s "
    view += "%s" % r

    return view % (num_bar, bar.low)

def volume_view(bar, ch_trend, num_bar):
    """Retorna a exibição com os volumes."""
    view = "%s %s %s"
    view += " %s" % r

    return view % (num_bar, ch_trend, bar.trend, bar.volume)

def range_view(bar, ch_trend, num_bar):
    """Retorna a view com os ranges das barras."""
    view = "%s %s %s"
    view += " %s" % r

    return view % (num_bar, ch_trend, bar.trend, bar.range)

def fib_view(c, trend):
    """Retorna a exibição de Fibonacci."""
    f = _helper.get_fib(c.high, c.low, c.trend)
    view = "%s %i"
    view += " %s %s %s * %s %s %s" % (r, r, r, r, r, r)
    return view % (trend, c.body, f.r61, f.r, f.r38, f.e38, f.e, f.e61)

def stat_view(bull, bear, doji):
    """ Retorna a view stat."""
    return "verde %i vermelho %i doji %i" % (bull, bear, doji)

# -*- coding: utf-8 -*-
from mtcli.pa.pa_one_bar import OneBar
from mtcli.pa import helpers as helper
from mtcli import conf


def brooks_view(bar, ch_trend, num_bar, brooks_pattern2, var_close):
    """Retorna a exibição com os padrões Brooks."""
    mp = helper.get_medium_point(bar)
    brooks1 = OneBar(bar.body, bar.top, bar.bottom, bar.close, mp)  # padrões de 1 barra

    tail = brooks1.tail
    if tail == conf.lbl_toptail:
        tail = "%s%i" % (tail, bar.top)
    if tail == conf.lbl_bottomtail:
        tail = "%s%i" % (tail, bar.bottom)

    view = "%s %s %s %s%iR%." + str(conf.digits) + "f %s %s"
    view += " %." + str(conf.digits) + "f"  # máxima
    view += " %." + str(conf.digits) + "f"  # mínima
    view += " %." + str(conf.digits) + "f"  # fechamento
    view += "MP%." + str(conf.digits) + "f"  # ponto médio
    view += " R%." + str(conf.digits) + "f %s"  # range, variação percentual

    return view % (
        num_bar,
        ch_trend,
        brooks1.pattern,
        brooks1.body_pattern,
        abs(bar.body),
        bar.body_range,
        brooks_pattern2,
        tail,
        bar.high,
        bar.low,
        bar.close,
        mp,
        bar.range,
        var_close,
    )


def ohlc_view(bar):
    """Retorna a view com o OHLC."""
    view = "%s"  # data
    view += " %." + str(conf.digits) + "f"  # abertura
    view += " %." + str(conf.digits) + "f"  # máxima
    view += " %." + str(conf.digits) + "f"  # mínima
    view += " %." + str(conf.digits) + "f"  # fechamento
    view += " %i"  # volume

    return view % (bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume)


def channel_view(bar, ch_trend, num_bar):
    """Retorna a exibição no formato de canal."""
    view = "%s %s"  # num da barra e tendencia do canal
    view += " %." + str(conf.digits) + "f"  # máxima
    view += " %." + str(conf.digits) + "f"  # mínima

    return view % (num_bar, ch_trend, bar.high, bar.low)


def close_view(bar, num_bar):
    """Retorna a view com os preços de fechamento."""
    view = "%s"  # tendência do canal
    view += " %." + str(conf.digits) + "f"  # fechamento

    return view % (num_bar, bar.close)


def high_view(bar, num_bar):
    """Retorna a view com as máximas."""
    view = "%s"  # tendência do canal
    view += " %." + str(conf.digits) + "f"  # máxima

    return view % (num_bar, bar.high)


def low_view(bar, num_bar):
    """Retorna a view com as mínimas."""
    view = "%s"  # tendência do canal
    view += " %." + str(conf.digits) + "f"  # mínima

    return view % (num_bar, bar.low)


def volume_view(bar, ch_trend, num_bar):
    """Retorna a view com os volumes."""
    return "%s %s %s %i" % (num_bar, ch_trend, bar.trend, bar.volume)


def range_view(bar, ch_trend, num_bar):
    """Retorna a view com os ranges das barras."""
    view = "%s %s %s"  # num da barra, tendencia do canal, tendencia da barra
    view += " %." + str(conf.digits) + "f"  # range

    return view % (num_bar, ch_trend, bar.trend, bar.range)


def stat_view(bull, bear, doji):
    """Retorna a view stat."""
    return "verde %i vermelho %i doji %i" % (bull, bear, doji)


def var_view(ch_trend, var, num_bar):
    """Retorna view com a variação percentual de duas barras."""
    return "%s %s %s" % (num_bar, ch_trend, var)

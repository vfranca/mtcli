"""
Formata as exibições
"""

from mtcli import conf
from mtcli.pa import pattern
from mtcli.pa import helpers


def view_min(bars):
    """Exibição mínima"""
    views = []
    n = 0
    corpo = []
    abert = []
    fech = []
    max = []
    min = []
    for bar in bars:
        n += 1
        corpo.append(bar.body)
        abert.append(bar.open)
        fech.append(bar.close)
        max.append(bar.high)
        min.append(bar.low)
        if len(min) == 2:
            padrao = pattern.TwoBars(corpo, abert, fech, max, min)
            direc = padrao.trend
            corpo.pop(0)
            abert.pop(0)
            fech.pop(0)
            max.pop(0)
            min.pop(0)
        else:
            direc = ""
        view = "%s %s"  # num da barra e tendencia do canal
        view += " %." + str(conf.digitos) + "f"  # máxima
        view += " %." + str(conf.digitos) + "f"  # mínima
        views.append(view % (n, direc, bar.high, bar.low))
    return views


def view_ranges(bars):
    "Exibição dos ranges" ""
    views = []
    n = 0
    corpo = []
    abert = []
    fech = []
    max = []
    min = []
    for bar in bars:
        n += 1
        corpo.append(bar.body)
        abert.append(bar.open)
        fech.append(bar.close)
        max.append(bar.high)
        min.append(bar.low)
        if len(min) == 2:
            padrao = pattern.TwoBars(corpo, abert, fech, max, min)
            direc = padrao.trend
            corpo.pop(0)
            abert.pop(0)
            fech.pop(0)
            max.pop(0)
            min.pop(0)
        else:
            direc = ""
        view = "%s %s %s"  # num da barra, tendencia do canal, tendencia da barra
        view += " %." + str(conf.digitos) + "f"  # range
        views.append(view % (n, direc, bar.trend, bar.range))
    return views


def view_full(bars):
    "Exibição completa" ""
    views = []
    n = 0
    corpo = []
    abert = []
    fech = []
    max = []
    min = []
    for bar in bars:
        n += 1
        corpo.append(bar.body)
        abert.append(bar.open)
        fech.append(bar.close)
        max.append(bar.high)
        min.append(bar.low)
        if len(min) == 2:
            padrao = pattern.TwoBars(corpo, abert, fech, max, min)
            gap = padrao.pattern
            direc = padrao.trend
            var_percent = helpers.get_var(fech[0], fech[1])
            corpo.pop(0)
            abert.pop(0)
            fech.pop(0)
            max.pop(0)
            min.pop(0)
        else:
            gap = ""
            direc = ""
            var_percent = ""
        mp = helpers.get_medium_point(bar)
        padrao = pattern.OneBar(
            bar.body, bar.top, bar.bottom, bar.close, mp
        )  # padrões de 1 barra
        sombra = padrao.tail
        if sombra == conf.toptail:
            sombra = "%s%i" % (sombra, bar.top)
        if sombra == conf.bottomtail:
            sombra = "%s%i" % (sombra, bar.bottom)
        view = "%s %s %s %s%iR%." + str(conf.digitos) + "f %s %s"
        view += " %." + str(conf.digitos) + "f"  # máxima
        view += " %." + str(conf.digitos) + "f"  # mínima
        view += " %." + str(conf.digitos) + "f"  # fechamento
        view += "MP%." + str(conf.digitos) + "f"  # ponto médio
        view += " R%." + str(conf.digitos) + "f %s"  # range, variação percentual
        views.append(
            view
            % (
                n,
                direc,
                padrao.pattern,
                padrao.body_pattern,
                abs(bar.body),
                bar.body_range,
                gap,
                sombra,
                bar.high,
                bar.low,
                bar.close,
                mp,
                bar.range,
                var_percent,
            )
        )
    return views


def view_ohlc(bars):
    "Exibição do OHLC" ""
    views = []
    n = 0
    for bar in bars:
        n += 1
        view = "%s"  # data
        view += " %." + str(conf.digitos) + "f"  # abertura
        view += " %." + str(conf.digitos) + "f"  # máxima
        view += " %." + str(conf.digitos) + "f"  # mínima
        view += " %." + str(conf.digitos) + "f"  # fechamento
        view += " %i"  # volume
        views.append(
            view % (bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume)
        )
    return views

"""
Formata as exibições
"""

from mtcli import conf
from mtcli.pa import pattern


def view_min(bars, count, num):
    """Exibição mínima"""
    views = []
    n = 0
    gaps, direcs, vars = get_padroes(bars)
    direcs = direcs[-count:]  # filtra quantidade de barras
    bars = bars[-count:]  # filtra quantidade de barras
    for bar, direc in zip(bars, direcs):
        n += 1
        if num:  # numerador de barra
            view = "%s %s"  # tendencia do canal
        else:
            view = "%s"  # tendencia do canal
        view += " %." + str(conf.digitos) + "f"  # máxima
        view += " %." + str(conf.digitos) + "f"  # mínima
        if num:
            views.append(view % (n, direc, bar.high, bar.low))
        else:
            views.append(view % (direc, bar.high, bar.low))
    return views


def view_ranges(bars, count, num):
    "Exibição dos ranges" ""
    views = []
    n = 0
    gaps, direcs, vars = get_padroes(bars)
    direcs = direcs[-count:]  # filtra quantidade de barras
    bars = bars[-count:]  # filtra quantidade de barras
    for bar, direc in zip(bars, direcs):
        n += 1
        if num:
            view = "%s %s %s"  # direção, direção da barra
        else:
            view = "%s %s"  # direção, direção da barra
        view += " %." + str(conf.digitos) + "f"  # range
        if num:
            views.append(view % (n, direc, bar.trend, bar.range))
        else:
            views.append(view % (direc, bar.trend, bar.range))
    return views


def view_full(bars, count, num):
    "Exibição completa" ""
    views = []
    n = 0
    gaps, direcs, vars = get_padroes(bars)
    direcs = direcs[-count:]  # filtra quantidade de barras
    gaps = gaps[-count:]  # filtra quantidade de barras
    vars = vars[-count:]  # filtra quantidade de barras
    bars = bars[-count:]  # filtra quantidade de barras
    for bar, direc, gap, var in zip(bars, direcs, gaps, vars):
        n += 1
        mp = get_medium_point(bar)
        padrao = pattern.OneBar(
            bar.body, bar.top, bar.bottom, bar.close, mp
        )  # padrões de 1 barra
        sombra = padrao.tail
        if sombra == conf.toptail:
            sombra = "%s%i" % (sombra, bar.top)
        if sombra == conf.bottomtail:
            sombra = "%s%i" % (sombra, bar.bottom)
        if num:
            view = "%s "
        else:
            view = ""
        view += "%s %s %s%iR%." + str(conf.digitos) + "f %s %s"
        view += " %." + str(conf.digitos) + "f"  # máxima
        view += " %." + str(conf.digitos) + "f"  # mínima
        view += " %." + str(conf.digitos) + "f"  # fechamento
        view += "MP%." + str(conf.digitos) + "f"  # ponto médio
        view += " R%." + str(conf.digitos) + "f %s"  # range, variação percentual
        if num:
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
                    var,
                )
            )
        else:
            views.append(
                view
                % (
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
                    var,
                )
            )
    return views


def view_ohlc(bars, count, num):
    "Exibição do OHLC" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if num:
            view = "%s "
        else:
            view = ""
        view += "%s"  # data
        view += " %." + str(conf.digitos) + "f"  # abertura
        view += " %." + str(conf.digitos) + "f"  # máxima
        view += " %." + str(conf.digitos) + "f"  # mínima
        view += " %." + str(conf.digitos) + "f"  # fechamento
        view += " %i"  # volume
        if num:
            views.append(
                view % (n, bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume)
            )
        else:
            views.append(
                view % (bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume)
            )
    return views


def view_var(bars, count, num):
    """Exibição de variações percentuais"""
    views = []
    n = 0
    gaps, direcs, vars = get_padroes(bars)
    vars = vars[-count:]  # filtra quantidade de barras
    bars = bars[-count:]  # filtra quantidade de barras
    for bar, var in zip(bars, vars):
        n += 1
        if num:
            view = "%s "
        else:
            view = ""
        view += "%.2f%%"  # variação percentual
        if num:
            views.append(view % (n, float(var)))
        else:
            views.append(view % (float(var)))
    return views


def view_open(bars, count, num):
    "Exibição de aberturas" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if num:
            view = "%s "
        else:
            view = ""
        view += "%." + str(conf.digitos) + "f"  # abertura
        if num:
            views.append(view % (n, bar.open))
        else:
            views.append(view % (bar.open))
    return views


def view_high(bars, count, num):
    "Exibição de maximas" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if num:
            view = "%s "
        else:
            view = ""
        view += "%." + str(conf.digitos) + "f"  # máxima
        if num:
            views.append(view % (n, bar.high))
        else:
            views.append(view % (bar.high))
    return views


def view_low(bars, count, num):
    "Exibição de minimas" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if num:
            view = "%s "
        else:
            view = ""
        view += "%." + str(conf.digitos) + "f"  # mínimas
        if num:
            views.append(view % (n, bar.low))
        else:
            views.append(view % (bar.low))
    return views


def view_close(bars, count, num):
    "Exibição de fechamentos" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if num:
            view = "%s "
        else:
            view = ""
        view += "%." + str(conf.digitos) + "f"  # fechamento
        if num:
            views.append(view % (n, bar.close))
        else:
            views.append(view % (bar.close))
    return views


def view_volume(bars, count, num):
    "Exibição de volumes" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if num:
            view = "%s "
        else:
            view = ""
        view += "%i"  # fechamento
        if num:
            views.append(view % (n, bar.volume))
        else:
            views.append(view % (bar.volume))
    return views


def get_padroes(bars):
    gaps = []
    direcs = []
    vars = []
    corpo = []
    abert = []
    fech = []
    max = []
    min = []
    for bar in bars:
        corpo.append(bar.body)
        abert.append(bar.open)
        fech.append(bar.close)
        max.append(bar.high)
        min.append(bar.low)
        if len(min) == 2:
            padrao = pattern.TwoBars(corpo, abert, fech, max, min)
            gap = padrao.pattern
            direc = padrao.trend
            var_percent = float(get_var(fech[0], fech[1]))
            corpo.pop(0)
            abert.pop(0)
            fech.pop(0)
            max.pop(0)
            min.pop(0)
        else:
            gap = ""
            direc = ""
            var_percent = 0
        gaps.append(gap)
        direcs.append(direc)
        vars.append(var_percent)
    return [gaps, direcs, vars]


def get_medium_point(bar):
    """Retorna o ponto médio da barra."""
    return round(bar.low + bar.range / 2, conf.digitos)


def get_var(price1, price2):
    """Calcula variação percentual de dois preços."""
    return round((price2 - price1) / price1 * 100, 2)

"""
Formata as exibições
"""

from mtcli import conf
from mtcli.pa import pattern


def view_min(bars, count):
    """Exibição mínima"""
    views = []
    n = 0
    gaps, direcs, vars = get_padroes(bars)
    direcs = direcs[-count:]  # filtra quantidade de barras
    bars = bars[-count:]  # filtra quantidade de barras
    for bar, direc in zip(bars, direcs):
        n += 1
        view = "%s %s"  # num da barra e tendencia do canal
        view += " %." + str(conf.digitos) + "f"  # máxima
        view += " %." + str(conf.digitos) + "f"  # mínima
        views.append(view % (n, direc, bar.high, bar.low))
    return views


def view_ranges(bars, count):
    "Exibição dos ranges" ""
    views = []
    n = 0
    gaps, direcs, vars = get_padroes(bars)
    direcs = direcs[-count:]  # filtra quantidade de barras
    bars = bars[-count:]  # filtra quantidade de barras
    for bar, direc in zip(bars, direcs):
        n += 1
        view = "%s %s %s"  # direção, direção da barra
        view += " %." + str(conf.digitos) + "f"  # range
        views.append(view % (n, direc, bar.trend, bar.range))
    return views


def view_full(bars, count):
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
                var,
            )
        )
    return views


def view_ohlc(bars, count):
    "Exibição do OHLC" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        view = "%s %s"  # data
        view += " %." + str(conf.digitos) + "f"  # abertura
        view += " %." + str(conf.digitos) + "f"  # máxima
        view += " %." + str(conf.digitos) + "f"  # mínima
        view += " %." + str(conf.digitos) + "f"  # fechamento
        view += " %i"  # volume
        views.append(
            view % (n, bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume)
        )
    return views


def view_var(bars, count):
    """Exibição de variações percentuais"""
    views = []
    n = 0
    gaps, direcs, vars = get_padroes(bars)
    vars = vars[-count:]  # filtra quantidade de barras
    bars = bars[-count:]  # filtra quantidade de barras
    for bar, var in zip(bars, vars):
        n += 1
        view = "%s %.2f%%"  # variação percentual
        views.append(view % (n, float(var)))
    return views


def view_open(bars, count):
    "Exibição de aberturas" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        view = "%s %." + str(conf.digitos) + "f"  # abertura
        views.append(view % (n, bar.open))
    return views


def view_high(bars, count):
    "Exibição de maximas" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        view = "%s %." + str(conf.digitos) + "f"  # máxima
        views.append(view % (n, bar.high))
    return views


def view_low(bars, count):
    "Exibição de minimas" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        view = "%s %." + str(conf.digitos) + "f"  # mínimas
        views.append(view % (n, bar.low))
    return views


def view_close(bars, count):
    "Exibição de fechamentos" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        view = "%s %." + str(conf.digitos) + "f"  # fechamento
        views.append(view % (n, bar.close))
    return views


def view_volume(bars, count):
    "Exibição de volumes" ""
    views = []
    n = 0
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        view = "%s %i"  # fechamento
        views.append(view % (n, bar.volume))
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

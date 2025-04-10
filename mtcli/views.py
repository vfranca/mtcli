"""
Formata as exibições
"""

from mtcli import conf
from mtcli.models import model_pattern
from mtcli.models import model_chart


def view_full(bars, count, period="d1", date="", numerator=False, show_date=False):
    "Exibição completa" ""
    views = []
    chart = model_chart.ChartModel(bars, len(bars), count, date)
    n = chart.get_n()
    gaps, direcs = chart.get_padroes()
    direcs = direcs[-count:]  # filtra quantidade de barras
    gaps = gaps[-count:]  # filtra quantidade de barras
    bars = bars[-count:]  # filtra quantidade de barras
    for bar, direc, gap in zip(bars, direcs, gaps):
        n += 1
        mp = get_medium_point(bar)
        padrao = model_pattern.OneBarModel(
            bar.body, bar.top, bar.bottom, bar.close, mp
        )  # padrões de 1 barra
        sombra = padrao.tail
        if sombra == conf.sombra_superior:
            sombra = "%s%i" % (sombra, bar.top)
        if sombra == conf.sombra_inferior:
            sombra = "%s%i" % (sombra, bar.bottom)
        if numerator or (
            show_date and (period == "d1" or period == "w1" or period == "mn1")
        ):  # numerador de barra ou data
            view = "%s "  # numerador ou data
        else:
            view = ""
        view += "%s %s %s%i %s %s"
        view += " %." + str(conf.digitos) + "f"  # máxima
        view += " %." + str(conf.digitos) + "f"  # mínima
        view += " %." + str(conf.digitos) + "f"  # fechamento
        view += conf.ponto_medio + "%." + str(conf.digitos) + "f"  # ponto médio
        view += " R%." + str(conf.digitos) + "f"  # range, variação percentual
        if show_date and (period == "d1" or period == "w1" or period == "mn1"):
            views.append(
                view
                % (
                    bar.date,
                    direc,
                    padrao.pattern,
                    padrao.body_pattern,
                    abs(bar.body),
                    gap,
                    sombra,
                    bar.high,
                    bar.low,
                    bar.close,
                    mp,
                    bar.range,
                )
            )
        elif numerator:
            views.append(
                view
                % (
                    n,
                    direc,
                    padrao.pattern,
                    padrao.body_pattern,
                    abs(bar.body),
                    gap,
                    sombra,
                    bar.high,
                    bar.low,
                    bar.close,
                    mp,
                    bar.range,
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
                    gap,
                    sombra,
                    bar.high,
                    bar.low,
                    bar.close,
                    mp,
                    bar.range,
                )
            )
    return views


def view_min(bars, count, period="d1", date="", numerator=False, show_date=False):
    """Exibição mínima"""
    views = []
    n = get_n(len(bars), count, date)
    gaps, direcs = get_padroes(bars)
    direcs = direcs[-count:]  # filtra quantidade de barras
    bars = bars[-count:]  # filtra quantidade de barras
    for bar, direc in zip(bars, direcs):
        n += 1
        if numerator or (
            show_date and (period == "d1" or period == "w1" or period == "mn1")
        ):  # numerador de barra ou data
            view = "%s "  # numerador ou data
        else:
            view = ""
        view += "%s %." + str(conf.digitos) + "f"  # máxima
        view += " %." + str(conf.digitos) + "f"  # mínima
        if show_date and (period == "d1" or period == "w1" or period == "mn1"):
            views.append(view % (bar.date, direc, bar.high, bar.low))
        elif numerator:
            views.append(view % (n, direc, bar.high, bar.low))
        else:
            views.append(view % (direc, bar.high, bar.low))
    return views


def view_ranges(bars, count, period="d1", date="", numerator=False, show_date=False):
    "Exibição dos ranges" ""
    views = []
    n = get_n(len(bars), count, date)
    gaps, direcs = get_padroes(bars)
    direcs = direcs[-count:]  # filtra quantidade de barras
    bars = bars[-count:]  # filtra quantidade de barras
    for bar, direc in zip(bars, direcs):
        n += 1
        if numerator or (
            show_date and (period == "d1" or period == "w1" or period == "mn1")
        ):  # numerador de barra ou data
            view = "%s "  # numerador ou data
        else:
            view = ""
        view += "%s %s %." + str(conf.digitos) + "f"  # range
        if show_date and (period == "d1" or period == "w1" or period == "mn1"):
            views.append(view % (bar.date, direc, bar.trend, bar.range))
        elif numerator:
            views.append(view % (n, direc, bar.trend, bar.range))
        else:
            views.append(view % (direc, bar.trend, bar.range))
    return views


def view_ohlc(bars, count, date="", numerator=False):
    "Exibição do OHLC" ""
    views = []
    n = get_n(len(bars), count, date)
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if numerator:
            view = "%s "
        else:
            view = ""
        view += "%s"  # data
        view += " %." + str(conf.digitos) + "f"  # abertura
        view += " %." + str(conf.digitos) + "f"  # máxima
        view += " %." + str(conf.digitos) + "f"  # mínima
        view += " %." + str(conf.digitos) + "f"  # fechamento
        view += " %i"  # volume
        if numerator:
            views.append(
                view % (n, bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume)
            )
        else:
            views.append(
                view % (bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume)
            )
    return views


def view_var(bars, count, period="d1", date="", numerator=False, show_date=False):
    """Exibição de variações percentuais"""
    views = []
    n = get_n(len(bars), count, date)
    vars_fech, vars_max, vars_min = get_vars(bars)
    vars_fech = vars_fech[-count:]  # filtra quantidade de barras
    vars_max = vars_max[-count:]  # filtra quantidade de barras
    vars_min = vars_min[-count:]  # filtra quantidade de barras
    bars = bars[-count:]  # filtra quantidade de barras
    for bar, var_fech, var_max, var_min in zip(bars, vars_fech, vars_max, vars_min):
        n += 1
        if numerator or (
            show_date and (period == "d1" or period == "w1" or period == "mn1")
        ):  # numerador de barra ou data
            view = "%s "  # numerador ou data
        else:
            view = ""
        view += "%.2f%% "  # variação percentual máxima
        view += "%.2f%% "  # variação percentual mínima
        view += "%.2f%%"  # variação percentual do fechamento
        if show_date and (period == "d1" or period == "w1" or period == "mn1"):
            views.append(
                view % (bar.date, float(var_max), float(var_min), float(var_fech))
            )
        elif numerator:
            views.append(view % (n, float(var_max), float(var_min), float(var_fech)))
        else:
            views.append(view % (float(var_max), float(var_min), float(var_fech)))
    return views


def view_volume(bars, count, period="d1", date="", numerator=False, show_date=False):
    "Exibição de volumes" ""
    views = []
    n = get_n(len(bars), count, date)
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if numerator or (
            show_date and (period == "d1" or period == "w1" or period == "mn1")
        ):  # numerador de barra ou data
            view = "%s "  # numerador ou data
        else:
            view = ""
        view += "%i"  # fechamento
        if show_date and (period == "d1" or period == "w1" or period == "mn1"):
            views.append(view % (bar.date, bar.volume))
        elif numerator:
            views.append(view % (n, bar.volume))
        else:
            views.append(view % (bar.volume))
    return views


def view_open(bars, count, period="d1", date="", numerator=False, show_date=False):
    "Exibição de aberturas" ""
    views = []
    n = get_n(len(bars), count, date)
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if numerator or (
            show_date and (period == "d1" or period == "w1" or period == "mn1")
        ):  # numerador de barra ou data
            view = "%s "  # numerador ou data
        else:
            view = ""
        view += "%." + str(conf.digitos) + "f"  # abertura
        if show_date and (period == "d1" or period == "w1" or period == "mn1"):
            views.append(view % (bar.date, bar.open))
        elif numerator:
            views.append(view % (n, bar.open))
        else:
            views.append(view % (bar.open))
    return views


def view_high(bars, count, period="d1", date="", numerator=False, show_date=False):
    "Exibição de maximas" ""
    views = []
    n = get_n(len(bars), count, date)
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if numerator or (
            show_date and (period == "d1" or period == "w1" or period == "mn1")
        ):  # numerador de barra ou data
            view = "%s "  # numerador ou data
        else:
            view = ""
        view += "%." + str(conf.digitos) + "f"  # máxima
        if show_date and (period == "d1" or period == "w1" or period == "mn1"):
            views.append(view % (bar.date, bar.high))
        elif numerator:
            views.append(view % (n, bar.high))
        else:
            views.append(view % (bar.high))
    return views


def view_low(bars, count, period="d1", date="", numerator=False, show_date=False):
    "Exibição de minimas" ""
    views = []
    n = get_n(len(bars), count, date)
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if numerator or (
            show_date and (period == "d1" or period == "w1" or period == "mn1")
        ):  # numerador de barra ou data
            view = "%s "  # numerador ou data
        else:
            view = ""
        view += "%." + str(conf.digitos) + "f"  # mínimas
        if show_date and (period == "d1" or period == "w1" or period == "mn1"):
            views.append(view % (bar.date, bar.low))
        elif numerator:
            views.append(view % (n, bar.low))
        else:
            views.append(view % (bar.low))
    return views


def view_close(bars, count, period="d1", date="", numerator=False, show_date=False):
    "Exibição de fechamentos" ""
    views = []
    n = get_n(len(bars), count, date)
    bars = bars[-count:]  # filtra quantidade de barras
    for bar in bars:
        n += 1
        if numerator or (
            show_date and (period == "d1" or period == "w1" or period == "mn1")
        ):  # numerador de barra ou data
            view = "%s "  # numerador ou data
        else:
            view = ""
        view += "%." + str(conf.digitos) + "f"  # fechamento
        if show_date and (period == "d1" or period == "w1" or period == "mn1"):
            views.append(view % (bar.date, bar.close))
        elif numerator:
            views.append(view % (n, bar.close))
        else:
            views.append(view % (bar.close))
    return views


def get_padroes(bars):
    """Retorna leituras de price action das barras."""
    gaps = []
    direcs = []
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
            padrao = model_pattern.TwoBarsModel(corpo, abert, fech, max, min)
            gap = padrao.pattern
            direc = padrao.trend
            corpo.pop(0)
            abert.pop(0)
            fech.pop(0)
            max.pop(0)
            min.pop(0)
        else:
            gap = ""
            direc = ""
        gaps.append(gap)
        direcs.append(direc)
    return [gaps, direcs]


def get_vars(bars):
    """Calcula variações percentuais das barras."""
    vars_fech = []
    vars_max = []
    vars_min = []
    fech = []
    max = []
    min = []
    for bar in bars:
        fech.append(bar.close)
        max.append(bar.high)
        min.append(bar.low)
        if len(min) == 2:
            var_fech = float(get_var(fech[0], fech[1]))
            var_max = float(get_var(fech[0], max[1]))
            var_min = float(get_var(fech[0], min[1]))
            fech.pop(0)
            max.pop(0)
            min.pop(0)
        else:
            var_fech = 0
            var_max = 0
            var_min = 0
        vars_fech.append(var_fech)
        vars_max.append(var_max)
        vars_min.append(var_min)
    return [vars_fech, vars_max, vars_min]


def get_medium_point(bar):
    """Retorna o ponto médio da barra."""
    return round(bar.low + bar.range / 2, conf.digitos)


def get_var(price1, price2):
    """Calcula variação percentual de dois preços."""
    return round((price2 - price1) / price1 * 100, 2)


def get_n(total_bars, count, date):
    """Número inicial do numerator"""
    n = 0
    if date:  # numerator para intraday
        n = total_bars - count
    if n < 0:  # não pode ser negativo
        n = 0
    return n

"""
Faz leituras de price action
"""

from mtcli import conf


def tipo_barra(h, l):
    """Verifica o tipo da barra."""
    # Verifica se é uma upbar
    # máxima mais alta e mínima mais alta ou igual
    if h[1] > h[0] and l[1] >= l[0]:
        return conf.up_bar
    # Verifica se é uma downbar
    # mínima mais baixa e máxima mais baixa ou igual
    if l[1] < l[0] and h[1] <= h[0]:
        return conf.down_bar
    # Verifica se é uma outside bar
    # máxima mais alta e mínima mais baixa
    if h[1] > h[0] and l[1] < l[0]:
        return conf.outside_bar
    # Verifica se é uma inside bar
    # máxima mais baixa ou igual e mínima mais alta ou igual
    if h[1] <= h[0] and l[1] >= l[0]:
        return conf.inside_bar


def gap_fechamento(c, h, l):
    """Retorna a string do gap de fechamento."""
    c1, c2 = c
    # Calcula o gap de fechamento da maxima anterior
    h1, h2 = h
    if c2 > h1:
        gap = c2 - h1
        return "G" + str(gap)
    # Calcula o gap de fechamento da mínima anterior
    l1, l2 = l
    if c2 < l1:
        gap = c2 - l1
        return "G" + str(gap)
    return ""


def variacao_percentual(c):
    """Retorna a string da variação percentual."""
    c1, c2 = c
    var = (c2 - c1) / c1 * 100
    var = round(var, 1)
    return str(var) + "%"


def range_barra(h, l):
    """Calcula o range da barra."""
    return h - l


def ponto_medio(h, l):
    """Calcula o ponto médio da barra."""
    return (h + l) / 2


def corpo(o, c):
    """Calcula o corpo da barra."""
    return c - o


def sombra_acima(h, o, c):
    """Calcula a sombra acima na barra."""
    if o > c:
        return h - o
    return h - c


def sombra_abaixo(l, o, c):
    """Calcula a sombra abaixo na barra."""
    if o > c:
        return c - l
    return o - l

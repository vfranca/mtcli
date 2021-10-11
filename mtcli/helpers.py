# -*- coding: utf-8 -*-
from mtcli import conf


def get_medium_point(bar):
    """Retorna o ponto médio da barra."""
    return round(bar.low + bar.range / 2, conf.digits)


def get_var(price1, price2):
    """Calcula variação percentual de dois preços."""
    return round((price2 - price1) / price1 * 100, 2)

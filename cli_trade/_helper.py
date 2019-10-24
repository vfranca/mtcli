# -*- coding: utf-8 -*-
from cli_trade import conf


def get_medium_point(bar):
    """ Retorna o ponto médio da barra."""
    return round(bar.low + bar.range / 2, conf.digits)

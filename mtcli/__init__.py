"""Aplicativo de linha de comando para exibir graficos do MetaTrader 5 em texto."""

from . import bars, conf, data, logger, models, views
from .extensions import media_movel, range_medio, volume_medio

# from .extensions import agressao


__version__ = "1.17.0"

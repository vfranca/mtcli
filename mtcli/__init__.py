"""Aplicativo de linha de comando para exibir graficos do MetaTrader 5 em texto."""

from . import bars, conf, data, logger, models, views
from .extensions import agressao, media_movel, moving_average, range_medio, volume_medio

__version__ = "1.14.1"

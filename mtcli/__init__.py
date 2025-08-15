"""Aplicativo de linha de comando para exibir graficos do MetaTrader 5 em texto."""

from . import bars, conf, data, logger, models, views
from .extensions import media_movel
from .extensions import range_medio
from .extensions import volume_medio
# from .extensions import moving_average
# from .extensions import agressao


__version__ = "1.14.6"

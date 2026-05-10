"""
Factory de views para renderização de barras.

Permite desacoplar controller da implementação concreta de visualização.
"""

from .full_view import FullView
from .hl_view import HlView
from .range_view import RangeView
from .rate_view import RateView
from .volume_view import VolumeView


class ViewFactory:
    """Factory de views para o comando bars."""

    MAP = {
        "full": FullView,
        "hl": HlView,
        "range": RangeView,
        "volume": VolumeView,
        "ohlc": RateView,
    }

    @classmethod
    def create(cls, name: str, **kwargs):
        try:
            return cls.MAP[name](**kwargs)
        except KeyError:
            raise ValueError(f"View desconhecida: {name}")

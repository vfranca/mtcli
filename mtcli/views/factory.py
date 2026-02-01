from mtcli.views.min import MinView
from mtcli.views.full import FullView
from mtcli.views.range import RangeView
from mtcli.views.rate import RateView
from mtcli.views.volume import VolumeView


class ViewFactory:
    """Factory de views para o comando bars."""

    MAP = {
        "min": MinView,
        "full": FullView,
        "range": RangeView,
        "volume": VolumeView,
        "rate": RateView,
    }

    @classmethod
    def create(cls, name: str, **kwargs):
        try:
            return cls.MAP[name](**kwargs)
        except KeyError:
            raise ValueError(f"View desconhecida: {name}")

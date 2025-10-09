"""Módulo da classe model para range médio."""

from mtcli import conf
from mtcli.models.bar_model import BarModel


class AverageRangeModel:
    """Classe model do range médio."""

    def __init__(self, rates, count):
        """Model do range médio."""
        self.rates = rates
        self.count = count
        self.ranges = self.get_ranges()

    def get_ranges(self):
        """Lista de ranges."""
        lista = []
        for rate in self.rates:
            bar = BarModel(rate)
            if bar.open == bar.high and bar.high == bar.low and bar.low == bar.close:
                continue  # elimina doji de 4 preços
            lista.append(bar.high - bar.low)
        return lista

    def average(self):
        """Calcula o range médio."""
        ranges = self.ranges[-self.count :]
        return round(sum(ranges) / len(ranges), conf.digitos)

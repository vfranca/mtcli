"""Módulo da classe model para range médio."""

from mtcli import conf
from mtcli.models import model_bar


class AverageRangeModel:
    """Classe model do range médio."""

    def __init__(self, rates, count):
        """Model do range médio."""
        self.rates = rates
        self.count = count
        self.lista = self.__lista()
        self.ar = self.__ar()

    def __lista(self):
        """Lista de ranges."""
        lista = []
        for rate in self.rates:
            bar = model_bar.BarModel(rate)
            if bar.open == bar.high and bar.high == bar.low and bar.low == bar.close:
                continue  # elimina doji de 4 preços
            lista.append(bar.high - bar.low)
        return lista

    def __ar(self):
        """Calcula o range médio."""
        ranges = self.lista[-self.count :]
        return round(sum(ranges) / len(ranges), conf.digitos)

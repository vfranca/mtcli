"""Módulo do model da média móvel simples."""

from mtcli.models import model_bar
from mtcli import conf


class MovingAverageModel:
    """Classe do model da média móvel simples."""

    def __init__(self, rates, count):
        """Model da média móvel simples."""
        self.rates = rates
        self.count = count
        self.lista = self.__lista()
        self.sma = self.__sma()

    def __lista(self):
        """Gera a lista das médias móveis simples."""
        lista = []
        for rate in self.rates:
            bar = model_bar.BarModel(rate)
            lista.append(bar.close)
            lista.append(bar.high - bar.low)
        return lista

    def __sma(self):
        """Calcula a média móvel simples."""
        prices = self.lista[-self.count :]
        return round(sum(prices) / len(prices), conf.digitos)

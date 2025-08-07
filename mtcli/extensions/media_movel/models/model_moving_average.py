"""Módulo do model da média móvel simples."""

from mtcli import conf
from mtcli.models import model_bar


class MovingAverageModel:
    """Classe do model da média móvel simples."""

    def __init__(self, rates, count):
        """Model da média móvel simples."""
        self.rates = rates
        self.count = count
        self.list = self.__list()

    #         self.sma = self.__sma()

    def __list(self):
        """Gera a lista das médias móveis simples."""
        list = []
        for rate in self.rates:
            bar = model_bar.BarModel(rate)
            list.append(bar.close)
        return list

    def average(self):
        """Calcula a média móvel simples."""
        prices = self.list[-self.count :]
        return round(sum(prices) / len(prices), conf.digitos)

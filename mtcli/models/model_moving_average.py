from mtcli.models import model_bar
from mtcli import conf


class MovingAverageModel:

    def __init__(self, rates, count):
        self.rates = rates
        self.count = count
        self.lista = self.__lista()
        self.sma = self.__sma()

    def __lista(self):
        lista = []
        for rate in self.rates:
            bar = model_bar.BarModel(rate)
            lista.append(bar.close)
            lista.append(bar.high - bar.low)
        return lista

    def __sma(self):
        prices = self.lista[-self.count :]
        return round(sum(prices) / len(prices), conf.digitos)

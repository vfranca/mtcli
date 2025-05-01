"""Módulo da classe model para volume médio."""

from mtcli import conf
from mtcli.models import model_bar


class VolumeMedioModel:
    """Classe model do volume médio."""

    def __init__(self, rates, count):
        """Model do volume médio."""
        self.rates = rates
        self.count = count
        self.lista = self.__lista()

    def __lista(self):
        """Lista dos volumes."""
        lista = []
        for rate in self.rates:
            bar = model_bar.BarModel(rate)
            lista.append(bar.volume)
        return lista

    def media(self):
        """Calcula o volume médio."""
        volumes = self.lista[-self.count :]
        return round(sum(volumes) / len(volumes), conf.digitos)

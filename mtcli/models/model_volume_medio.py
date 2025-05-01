"""Módulo da classe model para volume médio."""

from mtcli import conf
from mtcli.models import model_bar


class VolumeMedioModel:
    """Classe model do volume médio."""

    def __init__(self, rates, count, type):
        """Model do volume médio."""
        self.rates = rates
        self.count = count
        self.type = type
        self.list = self.__list()

    def __list(self):
        """Lista dos volumes."""
        list = []
        for rate in self.rates:
            bar = model_bar.BarModel(rate)
            if self.type == "tick":
                list.append(bar.volume)
            if self.type == "real":
                list.append(bar.volume_real)
        return list

    def media(self):
        """Calcula o volume médio."""
        volumes = self.list[-self.count :]
        return round(sum(volumes) / len(volumes), conf.digitos)

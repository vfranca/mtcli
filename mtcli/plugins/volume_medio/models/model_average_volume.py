"""Módulo da classe model para volume médio."""

from mtcli import conf
from mtcli.models.bar_model import BarModel


class AverageVolumeModel:
    """Classe model do volume médio."""

    def __init__(self, rates, count, type):
        """Model do volume médio."""
        self.rates = rates
        self.count = count
        self.type = type
        self.volumes = self.__get_volumes()

    def __get_volumes(self):
        """Lista dos volumes."""
        list = []
        for rate in self.rates:
            bar = BarModel(rate)
            if self.type == "tick":
                list.append(bar.volume)
            if self.type == "real":
                list.append(bar.volume_real)
        return list

    def average(self):
        """Calcula o volume médio."""
        volumes = self.volumes[-self.count :]
        return round(sum(volumes) / len(volumes), conf.digitos)

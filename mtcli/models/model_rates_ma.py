"""Módulo da classe da lista de cotações da média móvel."""

from mtcli import conf
from mtcli.models import csv_data


class RatesMaModel:
    """Classe model da lista das cotações da média móvel."""

    def __init__(self, symbol, period, count):
        """Model da lista das cotações da média móvel."""
        self.symbol = symbol
        self.period = period
        self.count = count
        self.file = self.__file()

    def __file(self):
        """Obtem o nome e o caminho do arquivo CSV das cotações da média móvel."""
        return (
            conf.csv_path + self.symbol + self.period + "-MA" + str(self.count) + ".csv"
        )

    def lista(self):
        """Gera a lista das cotações da média móvel."""
        return csv_data.get_data(self.file)

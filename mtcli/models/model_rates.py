"""Módulo da classe módel das cotações."""

from mtcli import conf
from mtcli import csv_data


class RatesModel:
    """Classe módel das cotações."""

    def __init__(self, symbol, period):
        """Model das cotações."""
        self.symbol = symbol
        self.period = period
        self.file = self.__file()
        self.lista = self.__lista()

    def __file(self):
        """Obtem o nome e caminho do arquivo CSV das cotações."""
        return conf.csv_path + self.symbol + self.period + ".csv"

    def __lista(self):
        """Gera a lista das cotações."""
        return csv_data.get_data(self.file)

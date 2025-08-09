"""Módulo do model rates."""

from mtcli.extensions.moving_average.data import CsvDataSource


class RatesModel:
    """Classe do model rates."""

    def __init__(self, symbol, period, count, source=None):
        """Construtor da classe model rates."""
        self.symbol = symbol
        self.period = period
        self.count = count
        self.source = source or CsvDataSource()
        self.lista = self.__get_data()

    def __get_data(self):
        """Obtem a lista das cotações."""
        return self.source.get_data(self.symbol, self.period, self.count)

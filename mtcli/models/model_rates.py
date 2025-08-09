"""Módulo do model para obtenção das cotações."""

from mtcli import conf


class RatesModel:
    """Classe do model para obtenção das cotações."""

    def __init__(self, symbol, period):
        """Construtor da classe model rates."""
        self.symbol = symbol.upper()
        self.period = period.upper()
        self.source = conf.get_data_source()
        self.lista = self.__get_data()

    def __get_data(self):
        """Obtem a lista das cotações."""
        return self.source.get_data(self.symbol, self.period)

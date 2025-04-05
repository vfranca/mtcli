from mtcli.models import csv_data
from mtcli import conf


class RatesModel:

    def __init__(self, symbol, period):
        self.symbol = symbol
        self.period = period
        self.file = self.__file()
        self.lista = self.__lista()

    def __file(self):
        return conf.csv_path + self.symbol + self.period + ".csv"

    def __lista(self):
        return csv_data.get_data(self.file)

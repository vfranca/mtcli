from mtcli.models import csv_data
from mtcli import conf


class RatesMaModel:

    def __init__(self, symbol, period, count):
        self.symbol = symbol
        self.period = period
        self.count = count
        self.file = self.__file()

    def __file(self):
        return (
            conf.csv_path + self.symbol + self.period + "-MA" + str(self.count) + ".csv"
        )

    def lista(self):
        return csv_data.get_data(self.file)

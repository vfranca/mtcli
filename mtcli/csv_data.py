"""
Importa para uma lista os dados da fonte CSV
"""
import csv
from mtcli import conf


class Data:

    data = []

    def __init__(self, symbol, period):
        csv_file = conf.csv_path + symbol + period + ".csv"
        with open(csv_file, encoding="utf-16", newline="") as f:
            lines = csv.reader(f, delimiter=",", quotechar="'")
            for line in lines:
                self.data.append(line)

    def __iter__(self):
        for item in self.data:
            yield item

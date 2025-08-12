"""Módulo fonte de dados via CSV."""

import csv
import os

from mtcli import conf
from mtcli.data.base import DataSourceBase


class CsvDataSource(DataSourceBase):
    """Fonte de dados via CSV."""

    def get_data(self, symbol, period, count):
        file_path = os.path.join(conf.csv_path, f"{symbol}{period}-ma{count}.csv")
        csv_data = []
        try:
            with open(file_path, encoding="utf-16", newline="") as f:
                lines = csv.reader(f, delimiter=",", quotechar="'")
                for line in lines:
                    csv_data.append(line)
        except:
            print("%s nao encontrado! Tente novamente" % file_path)
        return csv_data

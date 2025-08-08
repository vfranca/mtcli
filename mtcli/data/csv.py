import os
from mtcli import csv_data, conf
from .base import DataSourceBase


class CsvDataSource(DataSourceBase):
    """Fonte de dados via CSV."""

    def get_data(self, symbol, period):
        file_path = os.path.join(conf.csv_path, f"{symbol}{period}.csv")
        return csv_data.get_data(file_path)

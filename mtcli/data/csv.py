"""Módulo fonte de dados via CSV."""

import os
import csv
from mtcli import conf
from mtcli.logger import logger
from .base import DataSourceBase


class CsvDataSource(DataSourceBase):
    """Fonte de dados via CSV."""

    def get_data(self, symbol, period):
        """Retorna dados CSV em uma lista de lista."""
        file_path = os.path.join(conf.csv_path, f"{symbol}{period}.csv")
        logger.info(f"Iniciando coleta de dados via CSV: {file_path}.")
        csv_data = []
        try:
            with open(file_path, encoding="utf-16", newline="") as f:
                lines = csv.reader(f, delimiter=",", quotechar="'")
                for line in lines:
                    csv_data.append(line)
        except:
            logger.warning(f"Arquivo {file_path} não encontrado.")
            print("Arquivo %s nao encontrado! Tente novamente" % file_path)
        logger.info("Coleta de dados via CSV finalizada.")
        return csv_data

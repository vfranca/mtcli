"""
Módulo fonte de dados via CSV.
"""

import csv
import os

from mtcli.conf import conf
from mtcli.logger import setup_logger
from .base import DataSourceBase

logger = setup_logger(__name__)


class CsvDataSource(DataSourceBase):
    """Fonte de dados via CSV."""

    def __init__(self, base_path: str | None = None):
        """
        Args:
            base_path: caminho opcional para sobrescrever pasta padrão
        """
        self.base_path = base_path or conf.get_csv_path()

    def get_data(self, symbol, period, count=100):
        """
        Retorna dados CSV em formato padrão mtcli.

        Args:
            symbol (str)
            period (str)
            count (int)
        """
        file_path = os.path.join(self.base_path, f"{symbol}{period}.csv")

        logger.info("CSV | lendo arquivo: %s", file_path)

        csv_data = []

        try:
            with open(file_path, encoding="utf-16", newline="") as f:
                reader = csv.reader(f, delimiter=",", quotechar="'")

                for row in reader:
                    if not row:
                        continue
                    csv_data.append(row)

        except FileNotFoundError:
            logger.warning("Arquivo não encontrado: %s", file_path)
            return []

        except Exception as e:
            logger.exception("Erro ao ler CSV: %s", file_path)
            raise e

        # mantém apenas as últimas N barras (igual MT5)
        if count:
            csv_data = csv_data[-count:]

        logger.info("CSV | %s registros carregados", len(csv_data))

        return csv_data

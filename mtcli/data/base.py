"""
Módulo da classe base para coleta de dados.
"""

from typing import List


class DataSourceBase:
    """
    Interface base para fontes de dados.

    Todas as implementações devem retornar:

        List[
            [timestamp, open, high, low, close, tick_volume, real_volume]
        ]
    """

    def get_data(self, symbol: str, period: str, count: int = 100) -> List[list]:
        raise NotImplementedError("O método get_data deve ser implementado.")

"""Módulo da classe base para coleta de dados."""


class DataSourceBase:
    """Interface base para fontes de dados."""

    def get_data(self, symbol, period):
        """Retorna dados em uma lista de listas."""
        raise NotImplementedError("O método get_data deve ser implementado.")

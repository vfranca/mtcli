class DataSourceBase:
    """Interface base para fontes de dados."""

    def get_data(self, symbol, period):
        raise NotImplementedError("O método get_data deve ser implementado.")

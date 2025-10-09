"""Módulo do model para obtenção das cotações."""

from datetime import datetime

from mtcli import conf


class RatesModel:
    """Classe do model para obtenção das cotações."""

    def __init__(self, symbol, period, count=999, start=None, end=None, limit=None):
        """Construtor da classe model rates."""
        self.symbol = symbol
        self.period = period
        self.count = count
        self.start = start
        self.end = end
        self.limit = limit
        self.source = conf.get_data_source()

    def get_data(self):
        """Obtém a lista das cotações com filtros opcionais."""
        data = self.source.get_data(self.symbol, self.period, self.count)

        # Filtro por data
        if self.start or self.end:

            def filtrar(linha):
                datahora = datetime.strptime(linha[0], "%Y.%m.%d %H:%M:%S")
                if self.start and datahora < self.start:
                    return False
                if self.end and datahora > self.end:
                    return False
                return True

            data = list(filter(filtrar, data))
        # Limite de linhas
        if self.limit:
            data = data[-self.limit :]

        return data

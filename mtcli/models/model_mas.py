"""Módulo do model da média móvel."""

from mtcli.models import model_ma


class MasModel:
    """Classe model da lista de médias móveis."""

    def __init__(self, rates):
        """Model da lista das médias móveis."""
        self.rates = rates

    def lista(self):
        """Gera a lista  das médias móveis."""
        lista = []
        for rate in self.rates:
            ma = model_ma.MaModel(rate)
            lista.append(ma)
        return lista

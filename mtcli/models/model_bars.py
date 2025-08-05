"""Módulo da classe model da lista de barras."""

from mtcli.models import model_bar


class BarsModel:
    """Classe model da lista de barras."""

    def __init__(self, rates, date=""):
        """Model da lista de barras."""
        self.rates = rates
        self.date = date
        self.lista = self.__lista()

    def __lista(self):
        """Gera a lista das barras."""
        lista = []
        for rate in self.rates:
            bar = model_bar.BarModel(rate)
            if (
                self.date and str(bar.date) != self.date
            ):  # filtra por data para intraday
                continue
            lista.append(bar)
        return lista

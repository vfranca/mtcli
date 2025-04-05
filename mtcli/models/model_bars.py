from .model_bar import BarModel


class BarsModel:

    def __init__(self, rates, date):
        self.rates = rates
        self.date = date
        self.lista = self.__lista()

    def __lista(self):
        lista = []
        for rate in self.rates:
            bar = BarModel(rate)
            if (
                self.date and str(bar.date) != self.date
            ):  # filtra por data para intraday
                continue
            lista.append(bar)
        return lista

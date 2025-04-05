from .model_bar import BarModel


class RangesModel:

    def __init__(self, rates):
        self.rates = rates
        self.lista = self.__lista()

    def __lista(self):
        lista = []
        for rate in self.rates:
            bar = BarModel(rate)
            if bar.open == bar.high and bar.high == bar.low and bar.low == bar.close:
                continue  # elimina doji de 4 preços
            lista.append(bar.high - bar.low)
        return lista

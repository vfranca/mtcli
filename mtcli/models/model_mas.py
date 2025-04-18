from .model_ma import MaModel


class MasModel:

    def __init__(self, rates):
        self.rates = rates
        self.lista = self.__lista()

    def __lista(self):
        lista = []
        for rate in self.rates:
            ma = MaModel(rate)
            lista.append(ma)
        return lista

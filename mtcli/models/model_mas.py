from mtcli.models import model_ma


class MasModel:

    def __init__(self, rates):
        self.rates = rates

    def lista(self):
        lista = []
        for rate in self.rates:
            ma = model_ma.MaModel(rate)
            lista.append(ma)
        return lista

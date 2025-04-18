from mtcli import conf
from datetime import datetime


class MaModel:
    def __init__(self, rate):
        self.datetime = rate[0]
        self.date = self.__get_date()
        self.time = self.__get_time()
        self.close = float(rate[1])
        self.ma = float(rate[2])
        self.inclinacao = float(rate[3])
        self.variacao = float(rate[4])
        self.variacao_flat = int(rate[5])
        self.count = int(rate[6])
        self.mode = int(rate[7])
        self.price = int(rate[8])

    def __get_date(self):
        """Retorna a data da barra."""
        data = datetime.strptime(self.datetime, "%Y.%m.%d %H:%M:%S")
        return data.date()

    def __get_time(self):
        """Retorna o horário da barra."""
        hora = datetime.strptime(self.datetime, "%Y.%m.%d %H:%M:%S")
        return hora.time()

    def __get_body_range(self):
        """Retorna o tamanho absoluto do corpo."""
        return abs(self.close - self.open)

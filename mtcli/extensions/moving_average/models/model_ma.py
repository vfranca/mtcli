"""Módulo da classe model da média móvel."""

from datetime import datetime

from mtcli.extensions.moving_average import conf


class MaModel:
    """Classe model da média móvel."""

    def __init__(self, rate):
        """Model da média móvel."""
        self.datetime = rate[0]
        self.date = self.__get_date()
        self.time = self.__get_time()
        self.close = float(rate[1])
        self.ma = float(rate[2])
        self.inclinacao = str(rate[3])
        self.variacao = float(rate[4])
        self.variacao_flat = float(rate[5])
        self.count = int(rate[6])
        self.mode = str(rate[7])
        self.price = str(rate[8])

    def __get_date(self):
        """Obtem a data da média móvel no formato YYYY-MM-DD."""
        data = datetime.strptime(self.datetime, "%Y.%m.%d %H:%M:%S")
        return data.date()

    def __get_time(self):
        """Obtem o horário da média móvel no formato HH:MM:SS."""
        hora = datetime.strptime(self.datetime, "%Y.%m.%d %H:%M:%S")
        return hora.time()

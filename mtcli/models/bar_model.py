"""Módulo da classe model da barra."""

from datetime import datetime

from mtcli import conf


class BarModel:
    """Classe do model da barra."""

    def __init__(self, rate):
        """Model da barra."""
        self.datetime = rate[0]
        self.date = self.__get_date()
        self.time = self.__get_time()
        self.open = float(rate[1])
        self.high = float(rate[2])
        self.low = float(rate[3])
        self.close = float(rate[4])
        self.volume = int(rate[5])
        self.volume_real = int(rate[6])
        self.range = self.__get_range()
        self.body = self.__get_body()
        self.top = self.__get_top()
        self.bottom = self.__get_bottom()
        self.body_range = self.__get_body_range()
        self.trend = self.__get_trend()
        self.medium_point = self.__get_medium_point()

    def __get_date(self):
        """Obtem a data da barra no formato YYYY-MM-DD."""
        data = datetime.strptime(self.datetime, "%Y.%m.%d %H:%M:%S")
        return data.date()

    def __get_time(self):
        """Obtem o horário da barra no formato HH:MM:SS."""
        hora = datetime.strptime(self.datetime, "%Y.%m.%d %H:%M:%S")
        hora = hora.time()
        return hora.strftime("%H:%M")

    def __get_range(self):
        """Obtem o range da barra."""
        return self.high - self.low

    def __get_body(self):
        """Calcula o   range relativo do corpo da barra em porcentagem."""
        if self.range == 0:
            return 0

        return round((self.close - self.open) / self.range * 100)

    def __get_top(self):
        """Calcula o range relativo da sombra superior da barra em porcentagem."""
        high = self.high
        open = self.open
        close = self.close
        range = self.range

        if close >= open:
            top = high - close
        else:
            top = high - open

        if range == 0:
            return 0

        return round(top / range * 100)

    def __get_bottom(self):
        """Obtem o range relativo da sombra inferior da barra em porcentagem."""
        low = self.low
        open = self.open
        close = self.close
        range = self.range

        if close >= open:
            bottom = open - low
        else:
            bottom = close - low

        if range == 0:
            return 0

        return round(bottom / range * 100)

    def __get_body_range(self):
        """Calcula o range do corpo da barra."""
        return abs(self.close - self.open)

    def __get_trend(self):
        """Obtem a tendência da barra."""
        b = self.body

        if b > 0:
            trend = conf.alta
        elif b < 0:
            trend = conf.baixa
        else:
            trend = conf.lateral

        return trend

    def __get_medium_point(self):
        """Obtem o ponto médio da barra."""
        return round(self.low + self.range / 2, conf.digitos)

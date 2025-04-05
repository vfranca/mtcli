from mtcli import conf
from datetime import datetime


class BarModel(object):
    def __init__(self, rate):
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

    def __get_date(self):
        """Retorna a data da barra."""
        data = datetime.strptime(self.datetime, "%Y.%m.%d %H:%M:%S")
        return data.date()

    def __get_time(self):
        """Retorna o horário da barra."""
        hora = datetime.strptime(self.datetime, "%Y.%m.%d %H:%M:%S")
        return hora.time()

    def __get_range(self):
        """Retorna o range do candle."""
        return self.high - self.low

    def __get_body(self):
        """Retorna o tamanho  relativo do corpo real em porcentagem."""
        if self.range == 0:
            return 0

        return round((self.close - self.open) / self.range * 100)

    def __get_top(self):
        """Retorna o tamanho relativo da sombra superior em porcentagem."""
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
        """Retorna o tamanho relativo da sombra inferior em porcentagem."""
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
        """Retorna o tamanho absoluto do corpo."""
        return abs(self.close - self.open)

    def __get_trend(self):
        """Retorna a tendência da barra."""
        b = self.body

        if b > 0:
            trend = conf.alta
        elif b < 0:
            trend = conf.baixa
        else:
            trend = conf.lateral

        return trend

    def __str__(self):
        return "%s %.5f %.5f %.5f" % (self.body, self.high, self.low, self.close)

"""
Barra do gráfico
"""
from mtcli import conf


class Bar(object):
    def __init__(self, ohlc):
        self.open = float(ohlc[1])
        self.high = float(ohlc[2])
        self.low = float(ohlc[3])
        self.close = float(ohlc[4])
        self.volume = int(ohlc[5])
        self.datetime = ohlc[0]
        self.date = self.__get_date()
        self.range = self.__get_range()
        self.body = self.__get_body()
        self.top = self.__get_top()
        self.bottom = self.__get_bottom()
        self.body_range = self.__get_body_range()
        self.trend = self.__get_trend()

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
        "Retorna o tamanho absoluto do corpo." ""
        return abs(self.close - self.open)

    def __get_trend(self):
        b = self.body

        if b > 0:
            trend = conf.lbl_body_bull
        elif b < 0:
            trend = conf.lbl_body_bear
        else:
            trend = conf.lbl_body_doji

        return trend

    def __str__(self):
        return "%s %.5f %.5f %.5f" % (self.body, self.high, self.low, self.close)

    def __get_date(self):
        date = self.datetime.split(" ")
        return date[0]

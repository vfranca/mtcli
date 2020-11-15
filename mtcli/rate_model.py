"""
rate do array_rates
"""
from mtcli import conf


class RateModel(object):
    def __init__(self, row):
        self.datetime = row[0]
        self.open = float(row[1])
        self.high = float(row[2])
        self.low = float(row[3])
        self.close = float(row[4])
        self.ticks = int(row[5])
        self.volume = int(row[6])
        self.mm_curta = float(row[7])
        self.mm_curta_direcao = row[8]
        self.mm_intermediaria = float(row[9])
        self.mm_intermediaria_direcao = row[10]
        self.mm_longa = float(row[11])
        self.mm_longa_direcao = row[12]
        self.date = self.__get_date()
        self.range = self.__get_range()
        self.body = self.__get_body()
        self.top = self.__get_top()
        self.bottom = self.__get_bottom()
        self.body_range = self.__get_body_range()
        self.trend = self.__get_trend()

    def __get_range(self):
        """ Retorna o range do candle."""
        return self.high - self.low

    def __get_body(self):
        """ Retorna o tamanho  relativo do corpo real em porcentagem."""
        if self.range == 0:
            return 0

        return round((self.close - self.open) / self.range * 100)

    def __get_top(self):
        """ Retorna o tamanho relativo da sombra superior em porcentagem."""
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
        """ Retorna o tamanho relativo da sombra inferior em porcentagem."""
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

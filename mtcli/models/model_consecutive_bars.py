"""Módulo da classe model de leituras de barras consecutivas."""

from mtcli import conf


class ConsecutiveBarsModel:
    """Classe model da leitura de barras consecutivas."""

    def __init__(self, body, open, close, high, low, volume=[]):
        """Model da leitura de barras consecutivas."""
        self.body = body
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume

    def get_gap(self):
        """Leitura do gap de rompimento de duas barras."""
        if self.__is_gap():
            if self.body[1] > 0:
                gap = self.close[1] - self.high[0]
            if self.body[1] < 0:
                gap = self.low[0] - self.close[1]
            return gap
        return ""

    def __is_gap(self):
        """Verifica se existe gap de rompimento entre duas barras."""
        if self.body[1] == 0:
            return False
        if self.body[1] > 0 and self.close[1] <= self.high[0]:
            return False
        if self.body[1] < 0 and self.close[1] >= self.low[0]:
            return False
        return True

    def get_trend(self):
        """Leitura da tendência da sequência de duas barras."""
        if self.high[1] > self.high[0] and self.low[1] > self.low[0]:
            return conf.up_bar
        if self.high[1] < self.high[0] and self.low[1] < self.low[0]:
            return conf.down_bar
        if self.high[1] <= self.high[0] and self.low[1] >= self.low[0]:
            return conf.inside_bar
        if self.high[1] > self.high[0] and self.low[1] < self.low[0]:
            return conf.outside_bar
        return ""

    def volumes(self):
        """Comparação entre volumes consecutivos."""
        sequencia = ""
        if self.volume[1] > self.volume[0]:
            sequencia = "ASC"
        if self.volume[1] < self.volume[0]:
            sequencia = "DESC"
        return sequencia

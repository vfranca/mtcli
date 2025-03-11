"""
Leituras de padrões de price action
"""

from mtcli import conf


class OneBar(object):

    body_doji_max = conf.percentual_doji
    body_trend_min = conf.percentual_rompimento

    def __init__(self, body, top, bottom, close, retracement):
        self.body = body
        self.top = top
        self.bottom = bottom
        self.close = close
        self.retracement = retracement
        self.body_pattern = self.__get_body_pattern()
        self.tail = self.__get_tail()
        self.pattern = self.__get_pattern()

    def __get_body_pattern(self):
        """Padrão de corpo: alta/baixa/doji."""
        if abs(self.body) <= int(self.body_doji_max):
            return conf.lateral
        if self.body > 0:
            return conf.alta
        if self.body < 0:
            return conf.baixa

    def __get_tail(self):
        """Sombra sobressalente: TOPTAIL/BOTTOMTAIL/NEUTRAL."""
        if self.top > self.bottom:
            return conf.toptail
        if self.bottom > self.top:
            return conf.bottomtail
        return conf.notail

    def __get_pattern(self):
        """Padrão de uma barra: careca/topo raspado, fundo raspado."""
        if self.__is_buy_pressure():
            return conf.rompimento_alta
        if self.__is_sell_pressure():
            return conf.rompimento_baixa
        return ""

    def __is_buy_pressure(self):
        """Se tiver pressão compradora retorna true."""
        if self.body < 0:
            return False
        if abs(self.body) < self.body_trend_min:
            return False
        if self.close < self.retracement:
            return False
        if abs(self.body) >= 80:
            return True
        return True

    def __is_sell_pressure(self):
        """Se tiver pressão vendedora retorna true."""
        if self.body > 0:
            return False
        if abs(self.body) < self.body_trend_min:
            return False
        if self.close > self.retracement:
            return False
        if abs(self.body) >= 80:
            return True
        return True


class TwoBars(object):
    def __init__(self, body, open, close, high, low):
        self.body = body
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.trend = self.__get_trend()
        self.pattern = self.__get_pattern()

    def __get_pattern(self):
        """Padrão de duas barras."""
        # Verifica se existe gap
        if self.__is_gap():
            if self.body[1] > 0:
                gap = self.close[1] - self.high[0]
            if self.body[1] < 0:
                gap = self.low[0] - self.close[1]
            view = conf.gap + "%." + str(conf.digitos) + "f"
            return view % gap
        return ""

    def __is_gap(self):
        """Se for gap retorna true."""
        """ Se não tiver tendência retorna false."""
        if self.body[1] == 0:
            return False
        """ Na alta se o fechamento for menor ou igual à máxima anterior
        retorna false."""
        if self.body[1] > 0 and self.close[1] <= self.high[0]:
            return False
        """ Na baixa se o fechamento for maior ou igual à mínima anterior
        retorna false. """
        if self.body[1] < 0 and self.close[1] >= self.low[0]:
            return False
        return True

    def __get_trend(self):
        """Retorna a tendência da sequência de dois candles."""
        if self.high[1] > self.high[0] and self.low[1] > self.low[0]:
            return conf.up_bar
        if self.high[1] < self.high[0] and self.low[1] < self.low[0]:
            return conf.down_bar
        if self.high[1] <= self.high[0] and self.low[1] >= self.low[0]:
            return conf.inside_bar
        if self.high[1] > self.high[0] and self.low[1] < self.low[0]:
            return conf.outside_bar
        return ""

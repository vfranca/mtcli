"""
Padrões do método Al Brooks de 1 barra
"""
from mtcli import conf


class OneBar(object):

    body_doji_max = conf.percentual_lateral
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
        if abs(self.body) <= self.body_doji_max:
            return conf.lbl_body_doji
        if self.body > 0:
            return conf.lbl_body_bull
        if self.body < 0:
            return conf.lbl_body_bear

    def __get_tail(self):
        """Sombra sobressalente: TOPTAIL/BOTTOMTAIL/NEUTRAL."""
        if self.top > self.bottom:
            return conf.lbl_toptail
        if self.bottom > self.top:
            return conf.lbl_bottomtail
        return conf.lbl_tail_neutral

    def __get_pattern(self):
        """Padrão de uma barra: careca/topo raspado, fundo raspado."""
        if self.__is_buy_pressure():
            return conf.lbl_buy_pressure
        if self.__is_sell_pressure():
            return conf.lbl_sell_pressure
        return ""

    def __is_topo_careca(self):
        """Se for topo careca retorna true."""
        pass

    def __is_fundo_careca(self):
        """Se for fundo careca retorna true."""
        pass

    def __is_careca(self):
        """Se for careca retorna true."""
        pass

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

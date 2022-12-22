"""
Padrões do método Al Brooks de 2 barras
"""
from mtcli import conf


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
            view = "%s%." + str(conf.digits) + "f"
            return view % (conf.lbl_gap, gap)
        return conf.lbl_fbo

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

    def __is_bull_reversal(self):
        """Se for reversão de alta de duas barras retorna true."""
        pass

    def __is_bear_reversal(self):
        """Se for reversão de baixa de duas barras retorna true."""
        pass

    def __is_microdoubletop(self):
        """Se for micro topo duplo retorna true."""
        pass

    def __is_microdoublebottom(self):
        """Se for micro fundo duplo retorna true."""
        pass

    def __get_trend(self):
        """Retorna a tendência da sequência de dois candles."""
        if self.high[1] > self.high[0] and self.low[1] > self.low[0]:
            return conf.lbl_asc
        if self.high[1] < self.high[0] and self.low[1] < self.low[0]:
            return conf.lbl_desc
        if self.high[1] <= self.high[0] and self.low[1] >= self.low[0]:
            return conf.lbl_ib
        if self.high[1] > self.high[0] and self.low[1] < self.low[0]:
            return conf.lbl_ob
        return ""

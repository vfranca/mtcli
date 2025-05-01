"""Módulo da classe model das leituras de barra não consecutivas."""

from mtcli import conf


class UnconsecutiveBarModel:
    """Classe model das leituras de barra única."""

    body_doji_max = conf.percentual_doji
    body_trend_min = conf.percentual_rompimento

    def __init__(self, body, top, bottom, close, retracement):
        """Model das leituras de barra única."""
        self.body = body
        self.top = top
        self.bottom = bottom
        self.close = close
        self.retracement = retracement

    def get_body(self):
        """Leitura da tendência do corpo: alta/baixa/doji."""
        if abs(self.body) <= int(self.body_doji_max):
            return conf.lateral
        if self.body > 0:
            return conf.alta
        if self.body < 0:
            return conf.baixa

    def get_tail(self):
        """Leitura da maior sombra: superior/inferior."""
        if self.top > self.bottom:
            return conf.sombra_superior
        if self.bottom > self.top:
            return conf.sombra_inferior
        return ""

    def get_breakout(self):
        """Leitura da barra de rompimento."""
        if self.__is_bull_breakout():
            return conf.rompimento_alta
        if self.__is_bear_breakout():
            return conf.rompimento_baixa
        return ""

    def __is_bull_breakout(self):
        """Verifica se é uma barra de rompimento de alta."""
        if self.body < 0:
            return False
        if abs(self.body) < self.body_trend_min:
            return False
        if self.close < self.retracement:
            return False
        if abs(self.body) >= self.body_trend_min:
            return True
        return True

    def __is_bear_breakout(self):
        """Verifica se é uma barra de rompimento de baixa."""
        if self.body > 0:
            return False
        if abs(self.body) < self.body_trend_min:
            return False
        if self.close > self.retracement:
            return False
        if abs(self.body) >= self.body_trend_min:
            return True
        return True

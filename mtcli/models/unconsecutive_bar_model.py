"""Módulo da classe model das leituras de barra não consecutivas."""

from mtcli.conf import PERCENTUAL_BREAKOUT, PERCENTUAL_DOJI


class UnconsecutiveBarModel:
    """Classe model das leituras de barra única."""

    body_doji_max = PERCENTUAL_DOJI
    body_trend_min = PERCENTUAL_BREAKOUT

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
            return "doji"
        if self.body > 0:
            return "bull"
        if self.body < 0:
            return "bear"

    def get_tail(self):
        """Leitura da maior sombra: superior/inferior."""
        if self.top > self.bottom:
            return "top tail"
        if self.bottom > self.top:
            return "bottom tail"
        return ""

    def get_breakout(self):
        """Leitura da barra de rompimento."""
        if self.__is_bull_breakout():
            return "bull breakout"
        if self.__is_bear_breakout():
            return "bear breakout"
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

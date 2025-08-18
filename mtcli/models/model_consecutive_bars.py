"""Módulo da classe model de leituras de barras consecutivas."""

from mtcli import conf


class ConsecutiveBarsModel:
    """Classe model da leitura de barras consecutivas."""

    def __init__(self, bodys, opens, closes, highs, lows, volumes=[]):
        """Model da leitura de barras consecutivas."""
        self.bodys = bodys
        self.opens = opens
        self.closes = closes
        self.highs = highs
        self.lows = lows
        self.volumes = volumes

    def gap(self):
        """Leitura do gap de rompimento de duas barras."""
        if self.__is_gap():
            if self.bodys[1] > 0:
                gap = self.closes[1] - self.highs[0]
            if self.bodys[1] < 0:
                gap = self.lows[0] - self.closes[1]
            return gap
        return ""

    def __is_gap(self):
        """Verifica se existe gap de rompimento entre duas barras."""
        if self.bodys[1] == 0:
            return False
        if self.bodys[1] > 0 and self.closes[1] <= self.highs[0]:
            return False
        if self.bodys[1] < 0 and self.closes[1] >= self.lows[0]:
            return False
        return True

    def sequencia(self):
        """Leitura da tendência da sequência de duas barras."""
        if self.highs[1] > self.highs[0] and self.lows[1] > self.lows[0]:
            return conf.up_bar
        if self.highs[1] < self.highs[0] and self.lows[1] < self.lows[0]:
            return conf.down_bar
        if self.highs[1] <= self.highs[0] and self.lows[1] >= self.lows[0]:
            return conf.inside_bar
        if self.highs[1] > self.highs[0] and self.lows[1] < self.lows[0]:
            return conf.outside_bar
        return ""

    def volume(self):
        """Comparação entre volumes consecutivos."""
        sequencia = ""
        anterior = self.volumes[0]
        posterior = self.volumes[1]
        if posterior > anterior:
            sequencia = conf.alta
        if posterior < anterior:
            sequencia = conf.baixa
        return sequencia

    def continuacao(self):
        """Verifica se há continuação de movimento com corpo na mesma direção."""
        return self.bodys[0] * self.bodys[1] > 0 and abs(self.bodys[1]) > abs(
            self.bodys[0]
        )

    def reversao(self):
        """Verifica reversão pelo corpo oposto com maior intensidade."""
        return self.bodys[0] * self.bodys[1] < 0 and abs(self.bodys[1]) > abs(
            self.bodys[0]
        )

    def volume_spike(self, fator=2):
        """Detecta clímax de volume (volume da segunda barra bem maior)."""
        if len(self.volumes) < 2:
            return False
        return self.volumes[1] > self.volumes[0] * fator

"""Modulo da classe model da media movel."""


class MediaMovelModel:
    def __init__(self, closes, periodos=14):
        self.closes = [float(c) for c in closes]
        self.periodos = periodos

    def calcula_sma(self):
        return [
            sum(self.closes[i - self.periodos + 1 : i + 1]) / self.periodos
            for i in range(self.periodos - 1, len(self.closes))
        ]

    def calcula_ema(self):
        ema = []
        k = 2 / (self.periodos + 1)
        sma = sum(self.closes[: self.periodos]) / self.periodos
        ema.append(sma)
        for price in self.closes[self.periodos :]:
            ema.append(price * k + ema[-1] * (1 - k))
        return ema

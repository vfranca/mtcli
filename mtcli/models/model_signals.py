"""Lê os sinais gráficos nas barras."""

from mtcli import conf


class SignalsModel:
    """Lê sinais das barras."""

    def __init__(self, bars):
        self.bars = bars

    def get_sinais(self):
        """Retorna lista com todos os sinais por barra."""
        sinais = []
        entradas = []

        for i, bar in enumerate(self.bars):
            sinais_barra = []

            # Sinais de 1 barra
            if self.is_rompimento(bar):
                sinais_barra.append("rompimento")
            if self.is_doji(bar):
                sinais_barra.append("doji")

            # Sinais de 2 barras
            entradas.append(bar)
            if len(entradas) == 2:
                sequencia = self.get_sequencia(entradas)
                if sequencia:
                    sinais_barra.append(sequencia)
                gap = self.get_gap(entradas)
                if gap:
                    sinais_barra.append(gap)
                entradas.pop(0)

            sinais.append(sinais_barra or None)

        return sinais

    def is_rompimento(self, bar):
        return bar.body > 50

    def is_doji(self, bar):
        return bar.body <= 10

    def get_sequencia(self, bars):
        h1, h2 = bars[0].high, bars[1].high
        l1, l2 = bars[0].low, bars[1].low
        if h2 > h1 and l2 > l1:
            return "ascendente"
        elif h2 < h1 and l2 < l1:
            return "descendente"
        elif h2 <= h1 and l2 >= l1:
            return "interna"
        elif h2 > h1 and l2 < l1:
            return "externa"
        return None

    def get_gap(self, bars):
        bar1, bar2 = bars
        if bar2.body > 0 and bar2.low > bar1.high:
            return "gap de alta"
        elif bar2.body < 0 and bar2.high < bar1.low:
            return "gap de baixa"
        return None

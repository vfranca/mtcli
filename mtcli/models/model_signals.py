"""Lê sinais das barras."""

from mtcli import conf


class SignalsModel:
    """Lê sinais das barras."""

    def __init__(self, bars):
        """Construtor da classe."""
        self.bars = bars

    def get_sinais_de_uma_barra(self):
        """Retorna uma lista de sinais de 1 barra."""
        sinais = []

        for bar in self.bars:
            if self.is_rompimento(bar):
                sinais.append("rompimento")
            if self.is_doji(bar):
                sinais.append("doji")

        return sinais

    def is_rompimento(self, bar):
        """Verifica se é barra de rompimento."""
        return True if bar.body > 50 else False

    def is_doji(self, bar):
        """Verifica se é barra doji."""
        return True if bar.body <= 10 else False

    def get_sinais_de_duas_barras(self):
        """Retorna uma lista de sinais de 2 barras."""
        entradas = []
        sinais = []
        sinal = None
        for bar in self.bars:
            entradas.append(bar)
            if len(entradas) == 2:
                sinal = self.get_sequencia(entradas)
                entradas.pop(0)
            sinais.append(sinal) if sinal else sinais.append(None)

        return sinais

    def get_sequencia(self, bars):
        h1 = bars[0].high
        h2 = bars[1].high
        l1 = bars[0].low
        l2 = bars[1].low
        if h2 > h1 and l2 > l1:
            return "ascendente"
        elif h2 < h1 and l2 < l1:
            return "descendente"
        elif h2 <= h1 and l2 >= l1:
            return "interna"
        elif h2 > h1 and l2 < l1:
            return "externa"
        else:
            return None

    def get_gap(self, entradas):
        return "gap"

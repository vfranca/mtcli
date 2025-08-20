"""Lê os sinais gráficos nas barras."""

from mtcli import conf


class SignalsModel:
    """Lê sinais das barras."""

    def __init__(self, bars):
        self.bars = bars

    def get_sinais(self):
        """Retorna lista com sinais gráficos."""
        sinais = []
        inputs = []

        for bar in self.bars:
            lista_sinais = []

            # Sinais de 1 barra
            tipo = self.tipo(bar)
            if tipo:
                lista_sinais.append(tipo)
            else:
                lista_sinais.append(None)

            # Sinais de 2 barras
            inputs.append(bar)
            if len(inputs) == 2:
                continuacao = self.continuacao(inputs)
                if continuacao:
                    lista_sinais.append(continuacao)
                gap_barra = self.gap_barra(inputs)
                if gap_barra:
                    lista_sinais.append(gap_barra)
                gap_rompimento = self.gap_rompimento(inputs)
                if gap_rompimento:
                    lista_sinais.append(gap_rompimento)
                inputs.pop(0)

            sinais.append(lista_sinais or None)

        return sinais

    def tipo(self, bar):
        """Retorna o tipo da barra (rompimento/doji)."""
        if bar.body > 50:
            return "rompimento"
        elif bar.body <= 10:
            return "doji"
        else:
            return None

    def continuacao(self, bars):
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

    def gap_barra(self, bars):
        """Lê gap de barra (gap de alta/gap de baixa)."""
        bar1, bar2 = bars
        if bar2.body > 0 and bar2.low > bar1.high:
            return "gap de alta"
        elif bar2.body < 0 and bar2.high < bar1.low:
            return "gap de baixa"
        return None

    def gap_rompimento(self, bars):
        """Retorna gap de rompimento (gap de alta/gap de baixa)."""
        h1, l1 = bars[0].high, bars[0].low
        c2, t2 = bars[1].close, bars[1].trend.lower()
        if t2 == "verde" and c2 > h1:
            return "gap de alta"
        elif t2 == "vermelho" and c2 < l1:
            return "gap de baixa"
        else:
            return None

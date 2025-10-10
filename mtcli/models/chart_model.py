"""Módulo da classe model do gráfico."""

from mtcli.models.consecutive_bars_model import ConsecutiveBarsModel


class ChartModel:
    """Classe model do gráfico."""

    def __init__(self, bars, total_bars, count, date):
        """Model do gráfico."""
        self.bars = bars
        self.total_bars = total_bars
        self.count = count
        self.date = date

    def get_n(self):
        """Obtem o número inicial da numeração das barras."""
        n = 0
        if self.date:  # numerator para intraday
            n = self.total_bars - self.count
        if n < 0:  # não pode ser negativo
            n = 0
        return n

    def consecutive_sequencias(self):
        """Obtem lista da sequência de barras a partir da lista de barras."""
        sequencias = []
        bodys = []
        opens = []
        closes = []
        highs = []
        lows = []
        volumes = []
        for bar in self.bars:
            bodys.append(bar.body)
            opens.append(bar.open)
            closes.append(bar.close)
            highs.append(bar.high)
            lows.append(bar.low)
            volumes.append(bar.volume)
            if len(lows) == 2:
                consecutive = ConsecutiveBarsModel(
                    bodys, opens, closes, highs, lows, volumes
                )
                sequencia = consecutive.sequencia()
                bodys.pop(0)
                opens.pop(0)
                closes.pop(0)
                highs.pop(0)
                lows.pop(0)
                volumes.pop(0)
            else:
                sequencia = ""
            sequencias.append(sequencia)
        return sequencias

    def consecutive_gaps(self):
        """Obtem lista de gaps a partir da lista de barras."""
        gaps = []
        bodys = []
        opens = []
        closes = []
        highs = []
        lows = []
        volumes = []
        for bar in self.bars:
            bodys.append(bar.body)
            opens.append(bar.open)
            closes.append(bar.close)
            highs.append(bar.high)
            lows.append(bar.low)
            volumes.append(bar.volume)
            if len(lows) == 2:
                consecutive = ConsecutiveBarsModel(
                    bodys, opens, closes, highs, lows, volumes
                )
                gap = consecutive.gap()
                bodys.pop(0)
                opens.pop(0)
                closes.pop(0)
                highs.pop(0)
                lows.pop(0)
                volumes.pop(0)
            else:
                gap = ""
            gaps.append(gap)
        return gaps

    def consecutive_volumes(self, volume="tick"):
        """Obtem listas de leituras da sequência de volumes."""
        sequencias = []
        bodys = []
        opens = []
        closes = []
        highs = []
        lows = []
        volumes = []
        for bar in self.bars:
            bodys.append(bar.body)
            opens.append(bar.open)
            closes.append(bar.close)
            highs.append(bar.high)
            lows.append(bar.low)
            (
                volumes.append(bar.volume)
                if volume == "tick"
                else volumes.append(bar.volume_real)
            )
            if len(lows) == 2:
                consecutive = ConsecutiveBarsModel(
                    bodys, opens, closes, highs, lows, volumes
                )
                sequencia = consecutive.volume()
                bodys.pop(0)
                opens.pop(0)
                closes.pop(0)
                highs.pop(0)
                lows.pop(0)
                volumes.pop(0)
            else:
                sequencia = ""
            sequencias.append(sequencia)
        return sequencias

    def consecutive_vars(self):
        """Obtem a lista de variações percentuais entre os fechamentos das barras."""
        vars_fech = []
        vars_max = []
        vars_min = []
        fech = []
        max = []
        min = []
        for bar in self.bars:
            fech.append(bar.close)
            max.append(bar.high)
            min.append(bar.low)
            if len(min) == 2:
                var_fech = float(self._var_percent(fech[0], fech[1]))
                var_max = float(self._var_percent(fech[0], max[1]))
                var_min = float(self._var_percent(fech[0], min[1]))
                fech.pop(0)
                max.pop(0)
                min.pop(0)
            else:
                var_fech = 0
                var_max = 0
                var_min = 0
            vars_fech.append(var_fech)
            vars_max.append(var_max)
            vars_min.append(var_min)
        return [vars_fech, vars_max, vars_min]

    def _var_percent(self, price1, price2):
        """Calcula a variação percentual de dois fechamentos."""
        return round((price2 - price1) / price1 * 100, 2)

"""Módulo da classe model do gráfico."""

from mtcli.models import model_paction, model_consecutive_bars


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

    def consecutive_paction(self):
        """Obtem listas de leituras de price action da sequência de duas barras."""
        gaps = []
        direcs = []
        corpo = []
        abert = []
        fech = []
        max = []
        min = []
        for bar in self.bars:
            corpo.append(bar.body)
            abert.append(bar.open)
            fech.append(bar.close)
            max.append(bar.high)
            min.append(bar.low)
            if len(min) == 2:
                consecutive = model_consecutive_bars.ConsecutiveBarsModel(
                    corpo, abert, fech, max, min
                )
                gap = consecutive.get_gap()
                direc = consecutive.get_trend()
                corpo.pop(0)
                abert.pop(0)
                fech.pop(0)
                max.pop(0)
                min.pop(0)
            else:
                gap = ""
                direc = ""
            gaps.append(gap)
            direcs.append(direc)
        return [gaps, direcs]

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

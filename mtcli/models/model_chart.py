from mtcli.models import model_paction


class ChartModel:

    def __init__(self, bars, total_bars, count, date):
        self.bars = bars
        self.total_bars = total_bars
        self.count = count
        self.date = date

    def get_n(self):
        n = 0
        if self.date:  # numerator para intraday
            n = self.total_bars - self.count
        if n < 0:  # não pode ser negativo
            n = 0
        return n

    def get_padroes(self):
        """Retorna leituras de price action das barras."""
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
                pa = model_paction.TwoBarsModel(corpo, abert, fech, max, min)
                gap = pa.pattern
                direc = pa.trend
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

    def get_vars(self):
        """Calcula variações percentuais das barras."""
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
                var_fech = float(self.get_var(fech[0], fech[1]))
                var_max = float(self.get_var(fech[0], max[1]))
                var_min = float(self.get_var(fech[0], min[1]))
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

    def get_var(self, price1, price2):
        """Calcula variação percentual de dois preços."""
        return round((price2 - price1) / price1 * 100, 2)

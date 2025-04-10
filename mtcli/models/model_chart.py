from mtcli.models import model_pattern


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
                padrao = model_pattern.TwoBarsModel(corpo, abert, fech, max, min)
                gap = padrao.pattern
                direc = padrao.trend
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

from mtcli.models import model_pattern
from mtcli.models import model_chart
from mtcli import conf


class MinView:

    def __init__(self, bars, count, period = "d1", date = "", numerator = False, show_date = False):
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        chart = model_chart.ChartModel(bars, len(bars), count, date)
        self.n = chart.get_n()
        gaps, direcs = chart.get_padroes()
        self.direcs = direcs[-count:]
        self.bars = bars[-count:]

    def lista(self):
        views = []
        for bar, direc in zip(self.bars, self.direcs):
            self.n += 1
            if self.numerator or (
                self.show_date and (self.period == "d1" or self.period == "w1" or self.period == "mn1")
            ):  # numerador de barra ou data
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%s %." + str(conf.digitos) + "f"  # máxima
            view += " %." + str(conf.digitos) + "f"  # mínima
            if self.show_date and (self.period == "d1" or self.period == "w1" or self.period == "mn1"):
                views.append(view % (bar.date, direc, bar.high, bar.low))
            elif self.numerator:
                views.append(view % (self.n, direc, bar.high, bar.low))
            else:
                views.append(view % (direc, bar.high, bar.low))
        return views

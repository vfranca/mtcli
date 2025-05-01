"""Módulo da classe da view dos ranges."""

from mtcli import conf
from mtcli.models import model_chart


class RangesView:
    """Classe da view dos ranges."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        """View dos ranges."""
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = model_chart.ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Lista de views dos ranges."""
        views = []
        n = self.chart.get_n()
        gaps, direcs = self.chart.get_paction()
        direcs = direcs[-self.count :]
        for bar, direc in zip(self.bars, direcs):
            n += 1
            if self.numerator or self.show_date:
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%s %s %." + str(conf.digitos) + "f"  # range
            if self.show_date:
                if self.period == "d1" or self.period == "w1" or self.period == "mn1":
                    views.append(view % (bar.date, direc, bar.trend, bar.range))
                else:
                    views.append(view % (bar.time, direc, bar.trend, bar.range))
            elif self.numerator:
                views.append(view % (n, direc, bar.trend, bar.range))
            else:
                views.append(view % (direc, bar.trend, bar.range))
        return views

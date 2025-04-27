"""Módulo da classe da view de volumes."""

from mtcli.models import model_chart
from mtcli import conf


class VolumesView:
    """Classe da view de volumes."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        """View de volumes."""
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = model_chart.ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Retorna a lista de views."""
        views = []
        n = self.chart.get_n()
        for bar in self.bars:
            n += 1
            if self.numerator or self.show_date:
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%i"  # fechamento
            if self.show_date:
                if self.period == "d1" or self.period == "w1" or self.period == "mn1":
                    views.append(view % (bar.date, bar.volume))
                else:
                    views.append(view % (bar.time, bar.volume))
            elif self.numerator:
                views.append(view % (n, bar.volume))
            else:
                views.append(view % (bar.volume))
        return views

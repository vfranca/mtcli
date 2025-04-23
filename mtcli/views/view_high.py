"""Módulo da classe da view das máximas."""

from mtcli.models import model_chart
from mtcli import conf


class HighView:
    """Classe da view das máximas."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        """View das máximas."""
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = model_chart.ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Lista das views de máximas."""
        views = []
        n = self.chart.get_n()
        for bar in self.bars:
            n += 1
            if self.numerator or (
                self.show_date
                and (self.period == "d1" or self.period == "w1" or self.period == "mn1")
            ):  # numerador de barra ou data
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%." + str(conf.digitos) + "f"  # máxima
            if self.show_date and (
                self.period == "d1" or self.period == "w1" or self.period == "mn1"
            ):
                views.append(view % (bar.date, bar.high))
            elif self.numerator:
                views.append(view % (n, bar.high))
            else:
                views.append(view % (bar.high))
        return views

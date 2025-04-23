"""Módulo da classe da view dos fechamentos."""

from mtcli.models import model_chart
from mtcli import conf


class CloseView:
    """Classe da view dos fechamentos."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        """View dos fechamentos."""
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = model_chart.ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Lista das views de fechamento."""
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
                views.append(view % (bar.date, bar.close))
            elif self.numerator:
                views.append(view % (n, bar.close))
            else:
                views.append(view % (bar.close))
        return views

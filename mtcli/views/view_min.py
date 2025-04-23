"""Módulo da classe da view mínima."""

from mtcli.models import model_chart
from mtcli import conf


class MinView:
    """Classe da view mínima."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        """View mínima."""
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = model_chart.ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Lista das views mínimas."""
        views = []
        n = self.chart.get_n()
        gaps, direcs = self.chart.get_padroes()
        direcs = direcs[-self.count :]
        for bar, direc in zip(self.bars, direcs):
            n += 1
            if self.numerator or (
                self.show_date
                and (self.period == "d1" or self.period == "w1" or self.period == "mn1")
            ):  # numerador de barra ou data
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%s %." + str(conf.digitos) + "f"  # máxima
            view += " %." + str(conf.digitos) + "f"  # mínima
            if self.show_date and (
                self.period == "d1" or self.period == "w1" or self.period == "mn1"
            ):
                views.append(view % (bar.date, direc, bar.high, bar.low))
            elif self.numerator:
                views.append(view % (n, direc, bar.high, bar.low))
            else:
                views.append(view % (direc, bar.high, bar.low))
        return views

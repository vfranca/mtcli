"""Módulo da classe da view de mínimas."""

from mtcli import conf
from mtcli.models import model_chart


class LowView:
    """Classe da view das mínimas."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        """View das mínimas."""
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = model_chart.ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Lista das views das mínimas."""
        views = []
        n = self.chart.get_n()
        for bar in self.bars:
            n += 1
            if self.numerator or self.show_date:
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%." + str(conf.digitos) + "f"  # máxima
            if self.show_date:
                if self.period == "d1" or self.period == "w1" or self.period == "mn1":
                    views.append(view % (bar.date, bar.low))
                else:
                    views.append(view % (bar.time, bar.low))
            elif self.numerator:
                views.append(view % (n, bar.low))
            else:
                views.append(view % (bar.low))
        return views

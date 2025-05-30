"""Módulo da classe da view mínima."""

from mtcli import conf
from mtcli.models import model_chart


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
        sequencias = self.chart.consecutive_sequencias()
        sequencias = sequencias[-self.count :]
        for bar, sequencia in zip(self.bars, sequencias):
            n += 1
            if self.numerator or self.show_date:
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%s %." + str(conf.digitos) + "f"  # máxima
            view += " %." + str(conf.digitos) + "f"  # mínima
            if self.show_date:
                if self.period == "d1" or self.period == "w1" or self.period == "mn1":
                    views.append(view % (bar.date, sequencia, bar.high, bar.low))
                else:
                    views.append(view % (bar.time, sequencia, bar.high, bar.low))
            elif self.numerator:
                views.append(view % (n, sequencia, bar.high, bar.low))
            else:
                views.append(view % (sequencia, bar.high, bar.low))
        return views

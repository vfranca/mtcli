"""Módulo da classe da view de volumes."""

from mtcli import conf
from mtcli.models import model_chart


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
        sequencias = self.chart.consecutive_sequencias()
        sequencias = sequencias[-self.count :]
        sequencias_volume = self.chart.consecutive_volumes()
        sequencias_volume = sequencias_volume[-self.count :]
        for bar, sequencia, sequencia_volume in zip(
            self.bars, sequencias, sequencias_volume
        ):
            n += 1
            if self.numerator or self.show_date:
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%s %s %i"  # volume tick
            if self.show_date:
                if self.period == "d1" or self.period == "w1" or self.period == "mn1":
                    views.append(
                        view % (bar.date, sequencia, sequencia_volume, bar.volume)
                    )
                else:
                    views.append(
                        view % (bar.time, sequencia, sequencia_volume, bar.volume)
                    )
            elif self.numerator:
                views.append(view % (n, sequencia, sequencia_volume, bar.volume))
            else:
                views.append(view % (sequencia, sequencia_volume, bar.volume))
        return views

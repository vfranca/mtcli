"""Módulo da classe da view dos ranges."""

from mtcli import conf
from mtcli.models.chart_model import ChartModel


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
        self.chart = ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Lista de views dos ranges."""
        views = []
        n = self.chart.get_n()
        sequencias = self.chart.consecutive_sequencias()
        sequencias = sequencias[-self.count :]
        for bar, sequencia in zip(self.bars, sequencias):
            n += 1
            prefixo = f"{n} " if self.numerator else ""
            sufixo = ""
            if self.show_date:
                data = bar.date if self.period in {"d1", "w1", "mn1"} else bar.time
                sufixo = f" {data}"

            linha = (
                f"{prefixo}{sequencia} "
                f"{bar.trend} {bar.range:.{conf.digitos}f}"
                f"{sufixo}"
            )
            views.append(linha.upper())

        return views

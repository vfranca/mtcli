"""Módulo da classe da view mínima."""

from mtcli import conf
from mtcli.models import model_chart


class MinView:
    """Classe da view mínima."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = model_chart.ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        views = []
        n = self.chart.get_n()
        sequencias = self.chart.consecutive_sequencias()[-self.count :]

        for i, (bar, sequencia) in enumerate(zip(self.bars, sequencias), start=1):
            n += 1
            prefixo = ""
            if self.show_date:
                data = bar.date if self.period in {"d1", "w1", "mn1"} else bar.time
                prefixo = f"{data} "
            elif self.numerator:
                prefixo = f"{n} "

            linha = (
                f"{prefixo}{sequencia} "
                f"{bar.high:.{conf.digitos}f} "
                f"{bar.low:.{conf.digitos}f}"
            )
            views.append(linha)

        return views

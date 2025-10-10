"""Módulo da classe da view de mínimas."""

from mtcli import conf
from mtcli.models.chart_model import ChartModel


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
        self.chart = ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Lista das views das mínimas."""
        views = []
        n = self.chart.get_n()
        for bar in self.bars:
            n += 1
            prefixo = f"{n} " if self.numerator else ""
            sufixo = ""
            if self.show_date:
                data = bar.date if self.period in {"d1", "w1", "mn1"} else bar.time
                sufixo = f" {data}"

            linha = f"{prefixo}" f"{bar.low:.{conf.digitos}f}" f"{sufixo}"
            views.append(linha)

        return views

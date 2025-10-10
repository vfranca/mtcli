"""Módulo da view das cotações OHLC."""

from mtcli import conf
from mtcli.models.chart_model import ChartModel


class RatesView:
    """Classe da view das cotações OHLC."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        """View das cotações OHLC."""
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Lista das views de cotações OHLC."""
        views = []
        n = self.chart.get_n()
        for bar in self.bars:
            n += 1
            prefixo = f"{n} " if self.numerator else ""
            linha = (
                f"{prefixo}"
                f"{bar.date} "
                f"{bar.open:.{conf.digitos}f} "
                f"{bar.high:.{conf.digitos}f} "
                f"{bar.low:.{conf.digitos}f} "
                f"{bar.close:.{conf.digitos}f} "
                f"{bar.volume} "
                f"{bar.volume_real}"
            )
            views.append(linha)

        return views

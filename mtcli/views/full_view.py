"""Módulo da view completa."""

from mtcli.conf import BOTTOMTAIL, DIGITOS, TOPTAIL
from mtcli.models.chart_model import ChartModel
from mtcli.models.unconsecutive_bar_model import UnconsecutiveBarModel

from .utils import converte_nome


class FullView:
    """Classe da view completa."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        views = []
        n = self.chart.get_n()
        gaps = self.chart.consecutive_gaps()[-self.count :]
        sequencias = self.chart.consecutive_sequencias()[-self.count :]

        for i, (bar, gap, sequencia) in enumerate(
            zip(self.bars, gaps, sequencias), start=1
        ):
            n += 1
            ft_str = converte_nome(sequencia)
            ubar = UnconsecutiveBarModel(
                bar.body, bar.top, bar.bottom, bar.close, bar.medium_point
            )
            bo_str = converte_nome(ubar.get_breakout())
            trend_str = converte_nome(ubar.get_body())
            tail = ubar.get_tail()

            tail_str = ""
            if tail.lower() == "top tail":
                tail_str = f"{TOPTAIL}{bar.top}"
            elif tail.lower() == "bottom tail":
                tail_str = f"{BOTTOMTAIL}{bar.bottom}"

            gap_str = f"g{gap:.{DIGITOS}f}" if gap else ""
            corpo = abs(bar.body)

            prefixo = f"{n} " if self.numerator else ""
            sufixo = ""
            if self.show_date:
                data = bar.date if self.period in {"d1", "w1", "mn1"} else bar.time
                sufixo = f" {data}"

            linha = (
                f"{prefixo}{ft_str} "
                f"{bo_str} {trend_str}{corpo} "
                f"{gap_str} {tail_str} "
                f"{bar.high:.{DIGITOS}f} "
                f"{bar.low:.{DIGITOS}f} "
                f"{bar.close:.{DIGITOS}f}"
                f"m{bar.medium_point:.{DIGITOS}f} "
                f"R{bar.range:.{DIGITOS}f}{sufixo}"
            )
            views.append(linha.upper())

        return views

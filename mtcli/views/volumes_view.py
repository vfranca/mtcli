"""Módulo da classe da view de volumes."""

from mtcli import conf
from mtcli.models.chart_model import ChartModel


class VolumesView:
    """Classe da view de volumes."""

    def __init__(
        self,
        bars,
        count,
        period="d1",
        date="",
        numerator=False,
        show_date=False,
        volume="tick",
    ):
        """View de volumes."""
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.volume = volume
        self.chart = ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Retorna a lista de views."""
        views = []
        n = self.chart.get_n()
        sequencias = self.chart.consecutive_sequencias()
        sequencias = sequencias[-self.count :]
        sequencias_volume = self.chart.consecutive_volumes(self.volume)
        sequencias_volume = sequencias_volume[-self.count :]
        for bar, sequencia, sequencia_volume in zip(
            self.bars, sequencias, sequencias_volume
        ):
            n += 1
            volume = bar.volume if self.volume == "tick" else bar.volume_real
            prefixo = f"{n} " if self.numerator else ""
            sufixo = ""
            if self.show_date:
                data = bar.date if self.period in {"d1", "w1", "mn1"} else bar.time
                sufixo = f" {data}"

            linha = f"{prefixo}{sequencia} {sequencia_volume} {volume}" f"{sufixo}"
            views.append(linha.upper())

        return views

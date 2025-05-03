"""Módulo da classe da view intermediária."""

from mtcli import conf
from mtcli.models import model_chart, model_unconsecutive_bar


class IntermediateView:
    """Classe da view intermediária."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        """View intermediária."""
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = model_chart.ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Lista das views intermediárias."""
        views = []
        n = self.chart.get_n()
        sequencias = self.chart.consecutive_sequencias()
        sequencias = sequencias[-self.count :]
        for bar, sequencia in zip(self.bars, sequencias):
            n += 1
            unconsecutive = model_unconsecutive_bar.UnconsecutiveBarModel(
                bar.body, bar.top, bar.bottom, bar.close, bar.medium_point
            )  # leituras de uma barra não consecutiva
            trend = unconsecutive.get_body()
            if self.numerator or self.show_date:
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%s %s %i"  # sequenciaao, tendencia, corpo
            view += " %." + str(conf.digitos) + "f"  # máxima
            view += " %." + str(conf.digitos) + "f"  # mínima
            view += " R%." + str(conf.digitos) + "f"  # range, variação percentual
            if self.show_date:
                if self.period == "d1" or self.period == "w1" or self.period == "mn1":
                    views.append(
                        view
                        % (
                            bar.date,
                            sequencia,
                            trend,
                            abs(bar.body),
                            bar.high,
                            bar.low,
                            bar.range,
                        )
                    )
                else:
                    views.append(
                        view
                        % (
                            bar.time,
                            sequencia,
                            trend,
                            abs(bar.body),
                            bar.high,
                            bar.low,
                            bar.range,
                        )
                    )
            elif self.numerator:
                views.append(
                    view
                    % (
                        n,
                        sequencia,
                        trend,
                        abs(bar.body),
                        bar.high,
                        bar.low,
                        bar.range,
                    )
                )
            else:
                views.append(
                    view
                    % (
                        sequencia,
                        trend,
                        abs(bar.body),
                        bar.high,
                        bar.low,
                        bar.range,
                    )
                )
        return views

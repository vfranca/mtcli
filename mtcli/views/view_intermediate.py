"""Módulo da classe da view intermediária."""

from mtcli import conf
from mtcli.models import model_chart, model_paction


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
        gaps, direcs = self.chart.get_padroes()
        direcs = direcs[-self.count :]
        for bar, direc in zip(self.bars, direcs):
            n += 1
            pa = model_paction.BarModel(
                bar.body, bar.top, bar.bottom, bar.close, bar.medium_point
            )  # padrões de 1 barra
            trend = pa.get_body()
            if self.numerator or self.show_date:
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%s %s %i"  # direcao, tendencia, corpo
            view += " %." + str(conf.digitos) + "f"  # máxima
            view += " %." + str(conf.digitos) + "f"  # mínima
            view += " R%." + str(conf.digitos) + "f"  # range, variação percentual
            if self.show_date:
                if self.period == "d1" or self.period == "w1" or self.period == "mn1":
                    views.append(
                        view
                        % (
                            bar.date,
                            direc,
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
                            direc,
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
                        direc,
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
                        direc,
                        trend,
                        abs(bar.body),
                        bar.high,
                        bar.low,
                        bar.range,
                    )
                )
        return views

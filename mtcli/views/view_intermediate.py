from mtcli.models import model_paction
from mtcli.models import model_chart
from mtcli import conf


class IntermediateView:

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
        gaps, direcs = self.chart.get_padroes()
        gaps = gaps[-self.count :]
        direcs = direcs[-self.count :]
        for bar, gap, direc in zip(self.bars, gaps, direcs):
            n += 1
            pa = model_paction.BarModel(
                bar.body, bar.top, bar.bottom, bar.close, bar.medium_point
            )  # padrões de 1 barra
            trend = pa.get_body()
            if self.numerator or (
                self.show_date
                and (self.period == "d1" or self.period == "w1" or self.period == "mn1")
            ):  # numerador de barra ou data
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%s %s %i"  # direcao, tendencia, corpo
            if gap:
                view += " " + conf.gap + "%." + str(conf.digitos) + "f"
            else:
                view += " %s"
            view += " %." + str(conf.digitos) + "f"  # máxima
            view += " %." + str(conf.digitos) + "f"  # mínima
            view += " %." + str(conf.digitos) + "f"  # fechamento
            view += " R%." + str(conf.digitos) + "f"  # range, variação percentual
            if self.show_date and (
                self.period == "d1" or self.period == "w1" or self.period == "mn1"
            ):
                views.append(
                    view
                    % (
                        bar.date,
                        direc,
                        trend,
                        abs(bar.body),
                        gap,
                        bar.high,
                        bar.low,
                        bar.close,
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
                        gap,
                        bar.high,
                        bar.low,
                        bar.close,
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
                        gap,
                        bar.high,
                        bar.low,
                        bar.close,
                        bar.range,
                    )
                )
        return views

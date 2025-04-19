from mtcli.models import model_paction
from mtcli.models import model_chart
from mtcli import conf


class FullView:

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
            breakout = pa.get_breakout()
            body = pa.get_body()
            sombra = pa.get_tail()
            if sombra == conf.sombra_superior:
                sombra = "%s%i" % (sombra, bar.top)
            if sombra == conf.sombra_inferior:
                sombra = "%s%i" % (sombra, bar.bottom)
            if self.numerator or (
                self.show_date
                and (self.period == "d1" or self.period == "w1" or self.period == "mn1")
            ):  # numerador de barra ou data
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%s %s %s%i"
            if gap:
                view += " " + conf.gap + "%." + str(conf.digitos) + "f"
            else:
                view += " %s"
            view += " %s"
            view += " %." + str(conf.digitos) + "f"  # máxima
            view += " %." + str(conf.digitos) + "f"  # mínima
            view += " %." + str(conf.digitos) + "f"  # fechamento
            view += conf.ponto_medio + "%." + str(conf.digitos) + "f"  # ponto médio
            view += " R%." + str(conf.digitos) + "f"  # range, variação percentual
            if self.show_date and (
                self.period == "d1" or self.period == "w1" or self.period == "mn1"
            ):
                views.append(
                    view
                    % (
                        bar.date,
                        direc,
                        breakout,
                        body,
                        abs(bar.body),
                        gap,
                        sombra,
                        bar.high,
                        bar.low,
                        bar.close,
                        bar.medium_point,
                        bar.range,
                    )
                )
            elif self.numerator:
                views.append(
                    view
                    % (
                        n,
                        direc,
                        breakout,
                        body,
                        abs(bar.body),
                        gap,
                        sombra,
                        bar.high,
                        bar.low,
                        bar.close,
                        bar.medium_point,
                        bar.range,
                    )
                )
            else:
                views.append(
                    view
                    % (
                        direc,
                        breakout,
                        body,
                        abs(bar.body),
                        gap,
                        sombra,
                        bar.high,
                        bar.low,
                        bar.close,
                        bar.medium_point,
                        bar.range,
                    )
                )
        return views

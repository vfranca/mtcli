"""Módulo da classe da view completa."""

from mtcli.models import model_paction
from mtcli.models import model_chart
from mtcli import conf


class FullView:
    """Classe da view completa."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        """View completa."""
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = model_chart.ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Lista das views completas."""
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
            trend = pa.get_body()
            tail = pa.get_tail()
            if tail == conf.sombra_superior:
                tail = "%s%i" % (tail, bar.top)
            if tail == conf.sombra_inferior:
                tail = "%s%i" % (tail, bar.bottom)
            if self.numerator or self.show_date:
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%s %s %s%i"  # direcao, breakout, tendência, corpo
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
            if self.show_date:
                if self.period == "d1" or self.period == "w1" or self.period == "mn1":
                    views.append(
                        view
                        % (
                            bar.date,
                            direc,
                            breakout,
                            trend,
                            abs(bar.body),
                            gap,
                            tail,
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
                            bar.time,
                            direc,
                            breakout,
                            trend,
                            abs(bar.body),
                            gap,
                            tail,
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
                        trend,
                        abs(bar.body),
                        gap,
                        tail,
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
                        trend,
                        abs(bar.body),
                        gap,
                        tail,
                        bar.high,
                        bar.low,
                        bar.close,
                        bar.medium_point,
                        bar.range,
                    )
                )
        return views

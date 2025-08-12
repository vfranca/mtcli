"""Módulo da classe da view completa."""

from mtcli import conf
from mtcli.models import model_chart, model_consecutive_bars, model_unconsecutive_bar


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
        gaps = self.chart.consecutive_gaps()
        sequencias = self.chart.consecutive_sequencias()
        gaps = gaps[-self.count :]
        sequencias = sequencias[-self.count :]
        for bar, gap, sequencia in zip(self.bars, gaps, sequencias):
            n += 1
            unconsecutive = model_unconsecutive_bar.UnconsecutiveBarModel(
                bar.body, bar.top, bar.bottom, bar.close, bar.medium_point
            )  # padrões de 1 barra
            breakout = unconsecutive.get_breakout()
            trend = unconsecutive.get_body()
            tail = unconsecutive.get_tail()
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
                            sequencia,
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
                            sequencia,
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
                        sequencia,
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
                        sequencia,
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

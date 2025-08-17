from mtcli import conf
from mtcli.models import model_chart, model_unconsecutive_bar


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
        self.chart = model_chart.ChartModel(bars, len(bars), count, date)
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
            barra = model_unconsecutive_bar.UnconsecutiveBarModel(
                bar.body, bar.top, bar.bottom, bar.close, bar.medium_point
            )
            rompimento = barra.get_breakout()
            tendencia = barra.get_body()
            sombra = barra.get_tail()

            if sombra == conf.sombra_superior:
                sombra = f"{sombra}{bar.top}"
            elif sombra == conf.sombra_inferior:
                sombra = f"{sombra}{bar.bottom}"

            gap_str = f"{conf.gap}{gap:.{conf.digitos}f}" if gap else ""
            corpo = abs(bar.body)

            prefixo = f"{n} " if self.numerator else ""
            sufixo = ""
            if self.show_date:
                data = bar.date if self.period in {"d1", "w1", "mn1"} else bar.time
                sufixo = f" {data}"

            linha = (
                f"{prefixo}{sequencia} "
                f"{rompimento} {tendencia}{corpo} "
                f"{gap_str} {sombra} "
                f"{bar.high:.{conf.digitos}f} "
                f"{bar.low:.{conf.digitos}f} "
                f"{bar.close:.{conf.digitos}f}"
                f"{conf.ponto_medio}{bar.medium_point:.{conf.digitos}f} "
                f"R{bar.range:.{conf.digitos}f}{sufixo}"
            )
            views.append(linha)

        return views

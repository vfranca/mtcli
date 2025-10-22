"""Módulo da classe da view de variações percentuais."""

from mtcli.models.chart_model import ChartModel


class VarsView:
    """Classe da view de variações percentuais."""

    def __init__(
        self, bars, count, period="d1", date="", numerator=False, show_date=False
    ):
        """View de variações percentuais."""
        self.count = count
        self.period = period
        self.date = date
        self.numerator = numerator
        self.show_date = show_date
        self.chart = ChartModel(bars, len(bars), count, date)
        self.bars = bars[-count:]

    def views(self):
        """Lista das views de variações percentuais."""
        views = []
        n = self.chart.get_n()
        vars_fech, vars_max, vars_min = self.chart.consecutive_vars()
        vars_fech = vars_fech[-self.count :]  # filtra quantidade de barras
        vars_max = vars_max[-self.count :]  # filtra quantidade de barras
        vars_min = vars_min[-self.count :]  # filtra quantidade de barras
        for bar, var_fech, var_max, var_min in zip(
            self.bars, vars_fech, vars_max, vars_min
        ):
            n += 1
            var_max = float(var_max)
            var_min = float(var_min)
            var_fech = float(var_fech)

            prefixo = f"{n} " if self.numerator else ""
            sufixo = ""
            if self.show_date:
                data = bar.date if self.period in {"d1", "w1", "mn1"} else bar.time
                sufixo = f" {data}"

            linha = f"{prefixo}{var_max:.2f}% {var_min:.2f}% {var_fech:.2f}%{sufixo}"
            views.append(linha.upper())

        return views

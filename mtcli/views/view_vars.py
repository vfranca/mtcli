"""Módulo da classe da view de variações percentuais."""

from mtcli import conf
from mtcli.models import model_chart


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
        self.chart = model_chart.ChartModel(bars, len(bars), count, date)
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
            if self.numerator or self.show_date:
                view = "%s "  # numerador ou data
            else:
                view = ""
            view += "%.2f%% "  # variação percentual máxima
            view += "%.2f%% "  # variação percentual mínima
            view += "%.2f%%"  # variação percentual do fechamento
            if self.show_date:
                if self.period == "d1" or self.period == "w1" or self.period == "mn1":
                    views.append(
                        view
                        % (bar.date, float(var_max), float(var_min), float(var_fech))
                    )
                else:
                    views.append(
                        view
                        % (bar.time, float(var_max), float(var_min), float(var_fech))
                    )
            elif self.numerator:
                views.append(
                    view % (n, float(var_max), float(var_min), float(var_fech))
                )
            else:
                views.append(view % (float(var_max), float(var_min), float(var_fech)))
        return views

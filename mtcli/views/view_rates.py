from mtcli.models import model_pattern
from mtcli.models import model_chart
from mtcli import conf


class RatesView:

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
        for bar in self.bars:
            n += 1
            if self.numerator:
                view = "%s "
            else:
                view = ""
            view += "%s"  # data
            view += " %." + str(conf.digitos) + "f"  # abertura
            view += " %." + str(conf.digitos) + "f"  # máxima
            view += " %." + str(conf.digitos) + "f"  # mínima
            view += " %." + str(conf.digitos) + "f"  # fechamento
            view += " %i"  # volume
            if self.numerator:
                views.append(
                    view
                    % (n, bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume)
                )
            else:
                views.append(
                    view
                    % (bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume)
                )
        return views

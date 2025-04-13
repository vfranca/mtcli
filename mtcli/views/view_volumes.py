from mtcli.models import model_pattern
from mtcli.models import model_chart
from mtcli import conf


class VolumesView:

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
        direcs = direcs[-self.count :]
        for bar, direc in zip(self.bars, direcs):
            n += 1
        return views

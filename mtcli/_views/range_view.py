"""
View ranges
"""
from mtcli._views import view


class RangeView(view.View):
    def __init__(self, data_set):
        super().__init__(data_set)

    def set(self):
        txt = ""
        for data in self.data_set:
            txt += data.get("channel_trend")
            txt += " " + str(data.get("range"))
        self.view = txt

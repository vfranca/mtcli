"""
View dos ranges
"""
from mtcli.views import view


class RangeView(view.View):
    def __init__(self, data_set):
        super().__init__(data_set)

    def set(self):
        view = ""
        for data in self.data_set:
            pass
        self.view = view

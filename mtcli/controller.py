"""
FrontController
"""


class Controller:

    controller = "default"
    symbol = "ABEV3"
    period = "Daily"
    count = 1
    date = ""

    def __init__(self, controller="", symbol="", period="", count="", date=""):
        if controller:
            self.controller = controller
        if symbol:
            self.symbol = symbol
        if period:
            self.period = period
        if count:
            self.count = count
        if date:
            self.date = date
        self.get_model()
        self.get_view()

    def get_model(self):
        self.model = []

    def get_view(self):
        self.view = ""

    def __str__(self):
        return self.view

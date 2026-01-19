from mtcli.models.rates_model import RatesModel
from mtcli.models.bars_model import BarsModels
from .views.base_view import BaseView


class BarsController:

    def __init__(self, rates: RatesModel, bars: BarsModel, view: BaseView):
        rates = rates
        bars = bars
        view = view

    def run(self):
        rates = self.rates.get_data()
        bars = bars.get_datata()
        return view.render(bars)




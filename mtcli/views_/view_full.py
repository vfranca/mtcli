from mtcli.models import model_pattern
from mtcli.models import model_chart


class FullView(BaseView):

    def __init__(self, bars):
        self.bars = bars
        self.lista = self.__lista()

    def __lista(self):
        return self.padroes()

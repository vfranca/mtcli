"""
Model ranges
"""
from mtcli._models import model


class RangeModel(model.Model):
    def __init__(self, symbol="", period="", count=0, date=""):
        super().__init__(symbol, period, count, date)
        for rate in self.data_source:
            self.get(rate)
            data = {"high": self.high, "low": self.low, "range": self.range}
            self.data_set.append(data)
            
            #Limita o tamanho do data_set ao valor de count
            if self.count and len(self.data_set) > self.count:
                self.data_set.pop(0)


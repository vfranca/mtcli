from unittest import TestCase
from trade.src.chart import *
from trade.src.candle import Candle

class ChartTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"

    def test_chart_reader(self):
        self.assertTrue(chart_reader(self.file), "Retorno da função chart_reader")
    
    def test_date(self):
        bars = chart_reader(self.file)
        bar = Candle(bars[0])
        self.assertEqual(bar.date, "2018.01.04")

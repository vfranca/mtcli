from unittest import TestCase
from trade.src.reader import *
from trade.src.candle import Candle

class ReaderTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
        self.candles = chart_reader(self.file)
        self.candle = Candle(self.candles[4])

    def test_chart_reader(self):
        self.assertTrue(chart_reader(self.file), "Retorno da função chart_reader")
    
    def test_date(self):
        bars = chart_reader(self.file)
        bar = Candle(bars[0])
        self.assertEqual(bar.date, "2018.01.04")
    
    def test_trend(self):
        self.assertEqual(get_trend([4,5], [2,3]), "asc")
        self.assertEqual(get_trend([4,2], [3,1]), "desc")
        self.assertEqual(get_trend([4,3], [2,3]), "inside")
        self.assertEqual(get_trend([4,5], [2,1]), "outside")

    def test_show_default(self):
        self.assertEqual(get_show_default(self.candle), "  spin top 9 83241.0 83081.0 83161.0 * 83142.1 83161.0 83179.9 > 83302.1 83321.0 83339.9")



from unittest import TestCase
from trade.src.reader import *
from trade.src.candle import Candle

class ReaderTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
        self.candles = chart_reader(self.file)
        self.candle = Candle(self.candles[4])

    def test_file_exists(self):
        self.assertTrue(chart_reader(self.file))
    
    def test_date_filter(self):
        bars = chart_reader(self.file)
        bar = Candle(bars[0])
        self.assertEqual(bar.date, "2018.01.04")
    
    def test_asc(self):
        self.assertEqual(get_trend([4,5], [2,3]), "asc")
    def test_desc(self):
        self.assertEqual(get_trend([4,2], [3,1]), "desc")
    def test_inside(self):
        self.assertEqual(get_trend([4,3], [2,3]), "inside")

    def test_outside(self):
        self.assertEqual(get_trend([4,5], [2,1]), "outside")


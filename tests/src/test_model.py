from unittest import TestCase
from cli_trade.src.model import *
from cli_trade.src.helper import *
from cli_trade.src.candle import Candle

class ReaderTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
        self.candles = bar_model(self.file)
        self.candle = Candle(self.candles[4])

    def test_file_exists(self):
        self.assertTrue(bar_model(self.file))

    def test_date_filter(self):
        bars = bar_model(self.file)
        bar = Candle(bars[0])
        self.assertEqual(bar.date, "2018.01.04")

    #def test_asc(self):
        #self.assertEqual(get_trend([4,5], [2,3]), "ASC")
    #def test_desc(self):
        #self.assertEqual(get_trend([4,2], [3,1]), "DESC")
    #def test_inside(self):
        #self.assertEqual(get_trend([4,3], [2,3]), "IB")

    #def test_outside(self):
        #self.assertEqual(get_trend([4,5], [2,1]), "OB")


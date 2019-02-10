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

    def test_show_default(self):
        self.assertEqual(get_show_default(self.candle, "", ""), "  spin top 9 83241 83081 83161 * 83142 83161 83180 > 83302 83321 83340")

    def test_show_wdo(self):
        self.assertEqual(get_show_wdo(self.candle, "", ""), "  spin top 9 83241.0 83081.0 83161.0 * 83142.1 83161.0 83179.9 > 83302.1 83321.0 83339.9")

    def test_show_stock(self):
        self.assertEqual(get_show_stock(self.candle, "", ""), "  spin top 9 83241.00 83081.00 83161.00 * 83142.12 83161.00 83179.88 > 83302.12 83321.00 83339.88")

    def test_show_full(self):
        self.assertEqual(get_show_full(self.candle, "", ""), "  spin top 50 9 41 83146.00 83241.00 83081.00 83161.00 * 83142.12 83161.00 83179.88 > 83302.12 83321.00 83339.88")

    def test_show_channel(self):
        self.assertEqual(get_show_channel(self.candle, "asc", 100), "asc 83241.00 83081.00 > 83341.00 83181.00")
    
    def test_lt_diff(self):
        self.assertEqual(get_lt_diff([11,15], [2,8], "asc"), 6)
    
    def test_show_close(self):
        self.assertEqual(get_show_close(self.candle), "83161.00")

    def test_show_volume(self):
        self.assertEqual(get_show_volume(self.candle, "asc"), "asc 6794")

    def test_show_brooks(self):
        self.assertEqual(get_show_brooks(self.candle, "asc"), "asc lateral 9 83241.00 83081.00 83161.00")



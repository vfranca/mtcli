from unittest import TestCase
from trade.reader import *

class ReaderTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
    
    def test_show_default(self):
        candles = reader(self.file, times = 2)
        self.assertEqual(candles[0], "asc   73 92405 92330 92400 * 92359 92368 92376 > 92434 92442 92451")
    
    def test_show_channel(self):
        candles = reader(self.file, show = "channel")
        self.assertEqual(candles[1], "asc 83196.00 83096.00 > 83326.00 83226.00")
    
    def test_show_close(self):
        candles = reader(self.file, show = "close")
        self.assertEqual(candles[1], "83111.00")
    
    def test_show_volume(self):
        candles = reader(self.file, show = "vol")
        self.assertEqual(candles[1], "asc 3532")

    def test_show_brooks(self):
        candles = reader(self.file, show = "brooks")
        self.assertEqual(candles[1], "asc baixa -50 35 15 83196.00 83096.00 83111.00 * 83146.00 > 83046.00")

    def test_filtro_por_data(self):
        candles = reader(self.file, times = 2, date = "2018.09.13")
        self.assertEqual(candles[0], " engolfo alta  33 76244 76199 76229 * 76216 76222 76227 > 76261 76266 76272")
        candles = reader(self.file, date = "2018.09.13")
        self.assertEqual(candles[0], "   88 77359 77233 77344 * 77281 77296 77311 > 77407 77422 77437")
    



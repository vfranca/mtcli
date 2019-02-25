from unittest import TestCase
from trade.reader import *

class ReaderTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
    
    def test_show_default(self):
        candles = reader(self.file, times = 2)
        self.assertEqual(candles[0], "asc   73 92405 92330 92400 * 92368 92442")
    
    def test_show_channel(self):
        candles = reader(self.file, show = "channel")
        self.assertEqual(candles[1], "asc 83196 83096 * 83326 83226")
    
    def test_show_close(self):
        candles = reader(self.file, show = "close")
        self.assertEqual(candles[1], "83111")
    
    def test_show_volume(self):
        candles = reader(self.file, show = "vol")
        self.assertEqual(candles[1], "asc 3532")

    def test_show_brooks(self):
        candles = reader(self.file, show = "brooks")
        self.assertEqual(candles[1], " asc preto50 bottom15 83196 83096 83111 * 83146 83046")

    def test_filtro_por_data(self):
        candles = reader(self.file, times = 2, date = "2018.09.13")
        self.assertEqual(candles[0], " engolfo alta  33 76244 76199 76229 * 76222 76266")
        candles = reader(self.file, date = "2018.09.13")
        self.assertEqual(candles[0], "   88 77359 77233 77344 * 77296 77422")
    



from unittest import TestCase
from trade.reader import *

class ReaderTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
    
    def test_show(self):
        candles = reader(self.file, times = 2)
        self.assertEqual(candles[0], "asc  73 92405.0 92330.0 92400.0 * 92358.6 92367.5 92376.4 > 92433.6 92442.5 92451.4")
    
    def test_filtro_por_data(self):
        candles = reader(self.file, times = 2, date = "2018.09.13")
        self.assertEqual(candles[0], "  33 76244.0 76199.0 76229.0 * 76216.2 76221.5 76226.8 > 76261.2 76266.5 76271.8")
        candles = reader(self.file, date = "2018.09.13")
        self.assertEqual(candles[0], "  88 77359.0 77233.0 77344.0 * 77281.1 77296.0 77310.9 > 77407.1 77422.0 77436.9")
    



from unittest import TestCase
from trade.reader import *

class ReaderTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
    
    def test_filtro_por_data(self):
        candles = reader(self.file, times = 2, date = "2018.09.13")
        self.assertEqual(candles[0], "107  branco33  76244 76199 76229 r45 76222 76266")
        candles = reader(self.file, date = "2018.09.13")
        self.assertEqual(candles[0], "1  branco88 bottom0 77359 77233 77344 r126 77296 77422")
    



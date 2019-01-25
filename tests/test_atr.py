from unittest import TestCase
from trade.atr import *

class AtrTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
    
    def test_atr(self):
        self.assertEqual(atr(self.file, 14), 227.5)
    
    def test_limit(self):
        self.assertEqual([1, 2, 3, 4, 5][-2:], [4, 5])

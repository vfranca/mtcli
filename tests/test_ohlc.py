from unittest import TestCase
from trade import Ohlc

class OhlcTestCase(TestCase):

    def setUp(self):
        self.obj = Ohlc(['2015.04.01', '51187.00000', '56965.00000', '51187.00000', '56229.00000', '14628859', '8158109400'])

    def test_open(self):
        self.assertEqual(self.obj.open, 51187, "Preço de abertura")
    
    def test_close(self):
        self.assertEqual(self.obj.close, 56229, "Preço de fechamento")
    
    def test_hig(self):
        self.assertEqual(self.obj.high, 56965, "Preço máximo")
    
    def test_low(self):
        self.assertEqual(self.obj.low, 51187, "Preço mínimo")
    
if __name__ == '__main__':
    unittest.main()

from unittest import TestCase
from trade.src.candle import Candle

class CandleTestCase(TestCase):

    def setUp(self):
        self.obj = Candle(['2015.04.01', '51187.00000', '56965.00000', '51187.00000', '56229.00000', '14628859', '8158109400'])

    def test_size(self):
        self.assertEqual(self.obj.size, 5778, "Tamanho do candle")
    
    def test_real_body(self):
        self.assertEqual(self.obj.real_body, 0.87, "Corpo real do candle")
    
    def test_upper_shadow(self):
        self.assertEqual(self.obj.upper_shadow, 0.13, "Sombra superior do candle")
    
    def test_lower_shadow(self):
        self.assertEqual(self.obj.lower_shadow, 0.0, "Sombra inferior do candle")
    
    def test_trend(self):
        self.assertEqual(self.obj.trend, "alta", "Tendência")
    
    def test_high_trend_low(self):
        self.assertEqual(self.obj.high_trend_low(), "alta 56965.0 51187.0", "Saída no formato mácima tendência mínima")

if __name__ == '__main__':
    unittest.main()

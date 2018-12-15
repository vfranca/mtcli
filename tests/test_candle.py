from unittest import TestCase
from trade import Candle

class CandleTestCase(TestCase):

    def setUp(self):
        self.candle = Candle(['2015.04.01', '51187.00000', '56965.00000', '51187.00000', '56229.00000', '14628859', '8158109400'])

    def test_open(self):
        self.assertEqual(self.candle.open, 51187, "Preço de abertura")
    
    def test_close(self):
        self.assertEqual(self.candle.close, 56229, "Preço de fechamento")
    
    def test_hig(self):
        self.assertEqual(self.candle.high, 56965, "Preço máximo")
    
    def test_low(self):
        self.assertEqual(self.candle.low, 51187, "Preço mínimo")
    
    def test_size(self):
        self.assertEqual(self.candle.size, 5778, "Tamanho do candle")
    
    def test_real_body(self):
        self.assertEqual(self.candle.real_body, 5042, "Corpo real")
    
    def test_upper_shadow(self):
        self.assertEqual(self.candle.upper_shadow, 736, "Sombra superior")
    
    def test_lower_shadow(self):
        self.assertEqual(self.candle.lower_shadow, 0, "Sombra inferior")
    
    def test_trend(self):
        self.assertEqual(self.candle.trend, "alta", "Tendência")
    
    def test_high_trend_low(self):
        self.assertEqual(self.candle.high_trend_low(), "56965.0 alta 51187.0", "Saída no formato mácima tendência mínima")

if __name__ == '__main__':
    unittest.main()

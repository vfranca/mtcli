from unittest import TestCase
from trade import Candle

class CandleTestCase(TestCase):

    def setUp(self):
        self.candle = Candle("Abr72400.00Max72500.00Min72265.00Fch72320.00")

    def test_open(self):
        self.assertEqual(self.candle.open, 72400.00, "Preço de abertura")
    
    def test_close(self):
        self.assertEqual(self.candle.close, 72320.0, "Preço de fechamento")
    
    def test_max(self):
        self.assertEqual(self.candle.max, 72500.0, "Preço máximo")
    
    def test_min(self):
        self.assertEqual(self.candle.min, 72265.0, "Preço mínimo")
    
    def test_upper_shadow(self):
        self.assertEqual(self.candle.upper_shadow, 180, "Sombra superior")
    
    def test_lower_shadow(self):
        self.assertEqual(self.candle.lower_shadow, 135, "Sombra inferior")

if __name__ == '__main__':
    unittest.main()

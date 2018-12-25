from unittest import TestCase
from trade import Bar

class BarTestCase(TestCase):

    def setUp(self):
        self.obj = Bar(['2015.04.01', '51187.00000', '56965.00000', '51187.00000', '56229.00000', '14628859', '8158109400'])

    def test_size(self):
        self.assertEqual(self.obj.size, 5778, "Tamanho da barra")
    
    def test_body(self):
        self.assertEqual(self.obj.body, 0.87, "Corpo da barra")
    
    def test_upper_shadow(self):
        self.assertEqual(self.obj.upper_shadow, 0.13, "Sombra superior da barra")
    
    def test_lower_shadow(self):
        self.assertEqual(self.obj.lower_shadow, 0.0, "Sombra inferior da barra")
    
    def test_trend(self):
        self.assertEqual(self.obj.trend, "alta", "Tendência")
    
    def test_high_trend_low(self):
        self.assertEqual(self.obj.high_trend_low(), "alta 56965.0 51187.0", "Saída no formato mácima tendência mínima")

if __name__ == '__main__':
    unittest.main()

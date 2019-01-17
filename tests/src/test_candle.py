from unittest import TestCase
from trade.src.candle import Candle

class CandleTestCase(TestCase):

    def setUp(self):
        self.obj = Candle(['2015.04.01', '51187.00000', '56965.00000', '51187.00000', '56229.00000', '14628859', '8158109400'])
        self.obj1 = Candle(['2015.04.01 09:00', '51187.00000', '56965.00000', '51187.00000', '56229.00000', '14628859', '8158109400'])

    def test_open(self):
        self.assertEqual(self.obj.open, 51187, "Preço de abertura")
    
    def test_close(self):
        self.assertEqual(self.obj.close, 56229, "Preço de fechamento")
    
    def test_hig(self):
        self.assertEqual(self.obj.high, 56965, "Preço máximo")
    
    def test_low(self):
        self.assertEqual(self.obj.low, 51187, "Preço mínimo")
    
    def test_date(self):
        self.assertEqual(self.obj.date, "2015.04.01")
        self.assertEqual(self.obj1.date, "2015.04.01")
    
    def test_size(self):
        self.assertEqual(self.obj.size, 5778, "Tamanho da barra")
    
    def test_body(self):
        self.assertEqual(self.obj.body, 0.87, "Corpo da barra")
    
    def test_top_tail(self):
        self.assertEqual(self.obj.top_tail, 0.13, "Sombra superior da barra")
    
    def test_bottom_tail(self):
        self.assertEqual(self.obj.bottom_tail, 0.0, "Sombra inferior da barra")
    
    def test_trend(self):
        self.assertEqual(self.obj.trend, "alta", "Tendência")
    
    def test_str(self):
        self.assertEqual(self.obj.__str__(), "87 56965.0 51187.0 56229.0", "Saída no formato mácima tendência mínima")

if __name__ == '__main__':
    unittest.main()

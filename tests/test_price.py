from unittest import TestCase
from trade import Price

class PriceTestCase(TestCase):

    def setUp(self):
        self.obj = Price(88900.0, 87200.0, "h")
    
    def test_high(self):
        self.assertEqual(self.obj.h, 88900, "Máxima da vela")
    
    def test_low(self):
        self.assertEqual(self.obj.l, 87200, "Mínima da vela")
    
    def test_mediana(self):
        self.assertEqual(self.obj.m, 88050, "Mediana da vela")
    
    def test_fibo(self):
        self.assertEqual(self.obj.f, 87849.4, "Retração de 0,618 de Fibonacci")
    
    def test_projecao(self):
        self.assertEqual(self.obj.a, 89750, "Projeção de 100% a partir da mediana")
    
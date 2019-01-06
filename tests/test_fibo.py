from unittest import TestCase
from trade.fibo import Fibo

class FiboTestCase(TestCase):

    def setUp(self):
        self.obj = Fibo(88900.0, 87200.0, "h")
    
    def test_high(self):
        self.assertEqual(self.obj.h, 88900, "Máxima da vela")
    
    def test_low(self):
        self.assertEqual(self.obj.l, 87200, "Mínima da vela")
    
    def test_retracao_50(self):
        self.assertEqual(self.obj.r, 88050, "Retração de 0.50 de Fibonacci")
    
    def test_retracao_61(self):
        self.assertEqual(self.obj.r61, 87849.4, "Retração de 0,618 de Fibonacci")
    
    def test_extensao(self):
        self.assertEqual(self.obj.e, 89750, "Projeção de 100% ")
    
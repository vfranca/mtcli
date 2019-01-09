from unittest import TestCase
from trade.src.fib import Fib

class FibTestCase(TestCase):

    def setUp(self):
        self.obj = Fib(88900.0, 87200.0, "h")
    
    def test_high(self):
        self.assertEqual(self.obj.h, 88900, "Máxima do movimento")
    
    def test_low(self):
        self.assertEqual(self.obj.l, 87200, "Mínima do movimento")
    
    def test_retracao_38(self):
        self.assertEqual(self.obj.r38, 88250.6, "Retração de 0.382 de Fibonacci")
    
    def test_retracao_50(self):
        self.assertEqual(self.obj.r, 88050, "Retração de 0.50 de Fibonacci")
    
    def test_retracao_61(self):
        self.assertEqual(self.obj.r61, 87849.4, "Retração de 0,618 de Fibonacci")
    
    def test_extensao_61(self):
        self.assertEqual(self.obj.e61, 89950.6, "Extensão de 1.618 de Fibonacci")

    def test_extensao_50(self):
        self.assertEqual(self.obj.e, 89750, "Extensão de 0.50")

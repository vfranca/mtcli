from unittest import TestCase
from trade import Oco

class OcoTestCase(TestCase):

    def setUp(self):
        self.obj = Oco(89200.0, 88500.0, 88700.0)
    
    def test_cabeca(self):
        self.assertEqual(self.obj.c, 88500, "Cabeça do OCO")
    
    def test_pescoco(self):
        self.assertEqual(self.obj.p, 89200, "Pescoço do OCO")
    
    def test_ombro(self):
        self.assertEqual(self.obj.o, 88700, "Ombro direito do OCO")
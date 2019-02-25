from unittest import TestCase
from trade.src.brooks_patterns import BrooksPatterns

class BrooksPatternsTestCase(TestCase):

    def setUp(self):
        self.obj = BrooksPatterns(70, 25, 5)
        self.obj1 = BrooksPatterns(-70, 5, 25)
        self.obj2 = BrooksPatterns(-10, 50, 40)

    def test_body(self):
        self.assertEqual(self.obj.body, 70)
    
    def test_alta(self):
        self.assertEqual(self.obj.pattern, "branco")
    
    def test_baixa(self):
        self.assertEqual(self.obj1.pattern, "preto")

    def test_doji(self):
        self.assertEqual(self.obj2.pattern, "doji")
    
    def test_verde(self):
        self.assertEqual(self.obj.color, "verde")
    
    def test_vermelho(self):
        self.assertEqual(self.obj1.color, "vermelho")
    
    def test_top_tail(self):
        self.assertEqual(self.obj.tail, "bottom")
    
    def test_bottom_tail(self):
        self.assertEqual(self.obj1.tail, "top")
    

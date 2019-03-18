from unittest import TestCase
from trade.src.brooks_patterns1 import BrooksPatterns1

class BrooksPatterns1TestCase(TestCase):

    def setUp(self):
        self.o = BrooksPatterns1(50, 25, 25)

    def test_body_pattern_bull(self):
        o = BrooksPatterns1(50, 25, 25)
        self.assertEqual(o.body_pattern, "branco")
    
    def test_body_pattern_bear(self):
        o = BrooksPatterns1(-50, 25, 25)
        self.assertEqual(o.body_pattern, "preto")
    
    def test_body_pattern_doji(self):
        o = BrooksPatterns1(-5, 50, 45)
        self.assertEqual(o.body_pattern, "doji")

    def test_tail_top(self):
        o = BrooksPatterns1(-50, 20, 30)
        self.assertEqual(o.tail, "top")
    
    def test_tail_bottom(self):
        o = BrooksPatterns1(-50, 30, 20)
        self.assertEqual(o.tail, "bottom")
    
    def test_tail_neutral(self):
        o = BrooksPatterns1(-50, 25, 25)
        self.assertEqual(o.tail, "neutral")
    
    def test_buy_pressure(self):
        o = BrooksPatterns1(50, 25, 25)
        self.assertEqual(o.pattern, "forte")
    
    def test_sell_pressure(self):
        o = BrooksPatterns1(-50, 25, 25)
        self.assertEqual(o.pattern, "forte")
    



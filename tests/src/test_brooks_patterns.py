from unittest import TestCase
from trade.src.brooks_patterns import *

class BrooksPatternsTestCase(TestCase):

    def test_body_bull(self):
        self.assertEqual(get_body(70), "branco")
    
    def test_body_bear(self):
        self.assertEqual(get_body(-70), "preto")
    
    def test_body_doji(self):
        self.assertEqual(get_body(10), "doji")

    def test_tail_top(self):
        self.assertEqual(get_tail(10, 20), "topo")
    
    def test_tail_bottom(self):
        self.assertEqual(get_tail(20, 10), "fundo")
    
    def test_tail_none(self):
        self.assertEqual(get_tail(10, 10), "neutro")
    
    def test_bear_reversal(self):
        body = [50, -40]
        open = [3, 10]
        close = [10, 3]
        self.assertEqual(bear_reversal(body, open, close), "reversao baixa")

    def test_bull_reversal(self):
        body = [-40, 50]
        open = [10, 3]
        close = [3, 10]
        self.assertEqual(bull_reversal(body, open, close), "reversao alta")

    def test_get_pattern2(self):
        body = [-40, 50]
        open = [10, 3]
        close = [3, 10]
        self.assertEqual(get_pattern2(body, open, close), "reversao alta")



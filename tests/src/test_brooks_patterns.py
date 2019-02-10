from unittest import TestCase
from trade.src.brooks_patterns import BrooksPatterns

class BrooksPatternsTestCase(TestCase):

    def setUp(self):
        self.obj = BrooksPatterns(70)
        self.obj1 = BrooksPatterns(-70)
        self.obj2 = BrooksPatterns(-40)

    def test_body(self):
        self.assertEqual(self.obj.body, 70)
    
    def test_trend_bar_alta(self):
        self.assertEqual(self.obj.trend, "alta")
    
    def test_trend_bar_baixa(self):
        self.assertEqual(self.obj1.trend, "baixa")

    def test_trend_range_bar(self):
        self.assertEqual(self.obj2.trend, "lateral")
    
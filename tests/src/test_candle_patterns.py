from unittest import TestCase
from trade.src.candle_patterns import *

class CandlePatternsTestCase(TestCase):

    def test_is_doji(self):
        self.assertTrue(is_doji(3, 31, 66))
        self.assertTrue(is_doji(-3, 31, 66))
        self.assertFalse(is_doji(3, 30, 67))
        self.assertFalse(is_doji(-3, 30, 67))
        self.assertFalse(is_doji(0, 30, 70))
    
    def test_is_bullish_doji(self):
        self.assertTrue(is_bullish_doji(3, 27, 70))
        self.assertTrue(is_bullish_doji(-3, 27, 70))
        self.assertTrue(is_bullish_doji(1, 29, 70))
        self.assertTrue(is_bullish_doji(0, 30, 70))
    
    def test_is_dragon_fly_doji(self):
        self.assertTrue(is_dragon_fly_doji(3, 0, 97))
    
    def test_is_bearish_doji_test(self):
        self.assertTrue(is_bearish_doji(3, 70, 27))
        self.assertTrue(is_bearish_doji(-3, 70, 27))
    
    def test_is_gravestone_doji(self):
        self.assertTrue(is_gravestone_doji(3, 97, 0))
    
    def test_is_spinning_top(self):
        self.assertTrue(is_spinning_top(20, 40, 40))
        self.assertTrue(is_spinning_top(-20, 40, 40))
    
    def test_is_hammer(self):
        self.assertTrue(is_hammer(4, 21, 75))
        self.assertTrue(is_hammer(-4, 21, 75))
        self.assertFalse(is_hammer(3, 22, 75))
    


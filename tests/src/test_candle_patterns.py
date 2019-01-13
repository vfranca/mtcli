from unittest import TestCase
from trade.src.candle_patterns import *

class CandlePatternsTestCase(TestCase):

    def test_is_hammer(self):
        self.assertTrue(is_hammer(4, 21, 75))
        self.assertTrue(is_hammer(-4, 21, 75))
        self.assertFalse(is_hammer(3, 22, 75))
    
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
    
    def test_is_bearish_test(self):
        self.assertTrue(is_bearish_doji(3, 70, 27))
        self.assertTrue(is_bearish_doji(-3, 70, 27))
    

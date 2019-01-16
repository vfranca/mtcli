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
        self.assertFalse(is_dragon_fly_doji(0, 0, 0))
    
    def test_is_bearish_doji_test(self):
        self.assertTrue(is_bearish_doji(3, 70, 27))
        self.assertTrue(is_bearish_doji(-3, 70, 27))
    
    def test_is_gravestone_doji(self):
        self.assertTrue(is_gravestone_doji(3, 97, 0))
    
    def test_is_four_prices_doji(self):
        self.assertTrue(is_four_prices_doji(0, 0, 0))
    
    def test_is_marubozu(self):
        self.assertTrue(is_marubozu(100, 0, 0))
    
    def test_is_spinning_top(self):
        self.assertTrue(is_spinning_top(20, 40, 40))
        self.assertTrue(is_spinning_top(-20, 40, 40))
    
    def test_is_hammer(self):
        self.assertTrue(is_hammer(4, 29, 67))
        self.assertTrue(is_hammer(-4, 29, 67))
        self.assertTrue(is_hammer(-33, 0, 67))
        self.assertFalse(is_hammer(3, 30, 67))

    def test_is_inverted_hammer(self):
        self.assertTrue(is_inverted_hammer(4, 67, 29))
        self.assertTrue(is_inverted_hammer(-4, 67, 29))
        self.assertTrue(is_inverted_hammer(-33, 67, 0))
        self.assertFalse(is_inverted_hammer(3, 67, 30))


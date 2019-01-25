from unittest import TestCase
from trade.src.patterns import *

class PatternsTestCase(TestCase):

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

    def test_doji(self):
        self.assertEqual(get_pattern(1, 40, 59), "doji")

    def test_bullish_doji(self):
        bullish_doji = "doji alta"
        self.assertEqual(get_pattern(1, 29, 70), bullish_doji)
        self.assertEqual(get_pattern(-1, 29, 70), bullish_doji)
        self.assertEqual(get_pattern(0, 30, 70), bullish_doji)
    
    def test_dragon_fly_doji(self):
        dragon_fly_doji = "doji dragão"
        self.assertEqual(get_pattern(3, 0, 97), dragon_fly_doji)
        self.assertEqual(get_pattern(-3, 0, 97), dragon_fly_doji)
        self.assertEqual(get_pattern(0, 0, 100), dragon_fly_doji)

    def test_bearish_doji(self):
        bearish_doji = "doji baixa"
        self.assertEqual(get_pattern(1, 70, 29), bearish_doji)
        self.assertEqual(get_pattern(-1, 70, 29), bearish_doji)
        self.assertEqual(get_pattern(0, 70, 30), bearish_doji)
    
    def test_is_gravestone_doji(self):
        gravestone_doji = "doji lápide"
        self.assertEqual(get_pattern(3, 97, 0), gravestone_doji)
        self.assertEqual(get_pattern(-3, 97, 0), gravestone_doji)
        self.assertEqual(get_pattern(0, 100, 0), gravestone_doji)
    
    def test_four_prices_doji(self):
        self.assertEqual(get_pattern(0, 0, 0), "doji quat pre")
    
    def test_marubozu(self):
        self.assertEqual(get_pattern(100, 0, 0), "marubozu")
    
    def test_spinning_top(self):    
        spinning_top = "spin top"
        self.assertEqual(get_pattern(20, 40, 40), spinning_top)
        self.assertEqual(get_pattern(-20, 40, 40), spinning_top)
        self.assertEqual(get_pattern(4, 66, 40), spinning_top)
        self.assertEqual(get_pattern(4, 40, 66), spinning_top)

    def test_hammer(self):
        hammer = "martelo"
        self.assertEqual(get_pattern(10, 15, 75), hammer)
        self.assertEqual(get_pattern(-10, 15, 75), hammer)

    def test_inverted_hammer(self):
        inverted_hammer = "martinvert"
        self.assertEqual(get_pattern(10, 75, 15), inverted_hammer)
        self.assertEqual(get_pattern(-10, 75, 15), inverted_hammer)
    
    def test_bullish_engolfing(self):
        self.assertEqual(get_two_candles_pattern([-40, 80], [4, 1], [2, 6]), "engolfo alta")

    def test_bearish_engolfing(self):
        self.assertEqual(get_two_candles_pattern([40, -80], [2, 7], [6, 1]), "engolfo baixa")

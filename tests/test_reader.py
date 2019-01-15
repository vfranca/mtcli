from unittest import TestCase
from trade.reader import *

class ReaderTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
    
    def test_output(self):
        bars = reader(self.file, 2)
        self.assertEqual(bars[0], ' 73 92405.0 92330.0 92400.0 fib 92358.6 92367.5 92376.4 > 92433.6 92442.5 92451.4')
    
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



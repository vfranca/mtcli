from unittest import TestCase
from cli_trade.src.brooks_patterns2 import BrooksPatterns2
from tests.fixtures.settings import *

class BrooksPatterns2TestCase(TestCase):

    def setUp(self):
        self.o = BrooksPatterns2([50, 60], [10, 20], [40, 50], [60, 80], [5, 15])

    def test_close(self):
        self.assertEqual(self.o.close, [40, 50])

    def test_high(self):
        self.assertEqual(self.o.high, [60, 80])

    def test_low(self):
        self.assertEqual(self.o.low, [5, 15])

    def test_pattern_bear_gap(self):
        o = BrooksPatterns2([-50, -60], [90, 40], [20, 10], [80, 60], [15, 5])
        self.assertEqual(o.pattern, "%s5" % lbl_gap)


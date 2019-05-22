from unittest import TestCase
from cli_trade.src.brooks_patterns1 import BrooksPatterns1
from cli_trade.settings import *


class BrooksPatterns1TestCase(TestCase):

    def test_body_pattern_bull(self):
        o = BrooksPatterns1(50, 25, 25, 92600, 92500)
        self.assertEqual(o.body_pattern, lbl_body_bull)

    def test_body_pattern_bear(self):
        o = BrooksPatterns1(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.body_pattern, lbl_body_bear)

    def test_body_pattern_doji(self):
        o = BrooksPatterns1(-5, 50, 45, 92500, 92600)
        self.assertEqual(o.body_pattern, "DOJI")

    def test_tail_top(self):
        o = BrooksPatterns1(-50, 20, 30, 92500, 92600)
        self.assertEqual(o.tail, lbl_bottomtail)

    def test_tail_bottom(self):
        o = BrooksPatterns1(-50, 30, 20, 92500, 92600)
        self.assertEqual(o.tail, lbl_toptail)

    def test_tail_neutral(self):
        o = BrooksPatterns1(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.tail, lbl_tail_neutral)

    def test_buy_pressure(self):
        o = BrooksPatterns1(50, 20, 30, 92700, 92600)
        self.assertEqual(o.pattern, lbl_buy_pressure)

    def test_sell_pressure(self):
        o = BrooksPatterns1(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.pattern, lbl_sell_pressure)




import unittest
from mtcli.pa.pa_two_bars import TwoBars
from mtcli.conf import *


class TestTwoBars(unittest.TestCase):
    def setUp(self):
        self.o = TwoBars([50, 60], [10, 20], [40, 50], [60, 80], [5, 15])

    def test_close(self):
        self.assertEqual(self.o.close, [40, 50])

    def test_high(self):
        self.assertEqual(self.o.high, [60, 80])

    def test_low(self):
        self.assertEqual(self.o.low, [5, 15])

    def test_pattern_bear_gap(self):
        o = TwoBars([-50, -60], [90, 40], [20, 10], [80, 60], [15, 5])
        self.assertEqual(o.pattern, "%s5.00" % lbl_gap)


if __name__ == "__main__":
    unittest.main()

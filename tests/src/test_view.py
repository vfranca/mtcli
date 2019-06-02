from unittest import TestCase
from cli_trade.src.view import *
from cli_trade.src.model import *
from cli_trade.src.candle import Candle
from cli_trade.settings import *


class ViewTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
        self.candles = bar_model(self.file)
        self.candle = Candle(self.candles[4])

    def test_full(self):
        self.assertEqual(full_view(self.candle, "", ""), "  spin top 9 83146 83241 83081 83161 * 83161 83321")

    def test_channel(self):
        self.assertEqual(channel_view(self.candle, "asc", 1), "asc 83241 83081 1")

    def test_close(self):
        self.assertEqual(close_view(self.candle), "83161")

    def test_high(self):
        self.assertEqual(high_view(self.candle), "83241")

    def test_low(self):
        self.assertEqual(low_view(self.candle), "83081")

    def test_volume(self):
        self.assertEqual(volume_view(self.candle, "asc"), "asc 6794")

    def test_range(self):
        self.assertEqual(range_view(self.candle), "160")

    def test_brooks(self):
        self.assertEqual(brooks_view(self.candle, "ASC", 1, ""), "1 ASC  DOJI9R15  " + lbl_toptail + "50 83241 83081 83161 * 83161 83321")

    def test_fib(self):
        self.assertEqual(fib_view(self.candle, "asc"), "asc 9 83142 83161 83180 * 83302 83321 83340")



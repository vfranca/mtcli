from unittest import TestCase
from cli_trade.src.view import *
from cli_trade.src import view, model
from cli_trade.src.candle import Candle
from cli_trade.settings import *


class ViewTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
        self.candles = model.bar_model(self.file)
        self.candle = Candle(self.candles[4])

    def test_full(self):
        self.assertEqual(get_full(self.candle, "", ""), "  spin top 9 83146 83241 83081 83161 * 83161 83321")

    def test_channel(self):
        self.assertEqual(get_channel(self.candle, "asc", 1), "asc 83241 83081 1")

    def test_close(self):
        self.assertEqual(get_close(self.candle), "83161")

    def test_high(self):
        self.assertEqual(get_high(self.candle), "83241")

    def test_low(self):
        self.assertEqual(get_low(self.candle), "83081")

    def test_volume(self):
        self.assertEqual(get_volume(self.candle, "asc"), "asc 6794")

    def test_range(self):
        self.assertEqual(get_range(self.candle), "160")

    def test_brooks(self):
        self.assertEqual(get_brooks(self.candle, "ASC", 1, ""), "1 ASC  DOJI9R15  " + lbl_toptail + "50 83241 83081 83161 * 83161 83321")

    def test_fib(self):
        self.assertEqual(view.get_fib(self.candle, "asc"), "asc 9 83142 83161 83180 * 83302 83321 83340")



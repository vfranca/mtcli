#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from cli_trade.src.candle import Candle


class CandleEurUsdTestCase(TestCase):

    def setUp(self):
        self.obj = Candle([
            '2019.04.29 06:00:00',
            '1.11575',
            '1.11575',
            '1.11569',
            '1.11569',
            '25',
            '0'
        ])

    def test_open(self):
        self.assertEqual(self.obj.open, 1.11575)

    def test_close(self):
        self.assertEqual(self.obj.close, 1.11569)

    def test_hig(self):
        self.assertEqual(self.obj.high, 1.11575)

    def test_low(self):
        self.assertEqual(self.obj.low, 1.11569)

    def test_date(self):
        self.assertEqual(self.obj.date, "2019.04.29")

    def test_range(self):
        self.assertEqual(self.obj.range, 0.00006)

    def test_body(self):
        self.assertEqual(self.obj.body, -100)

    def test_top(self):
        self.assertEqual(self.obj.top, 0.0, "Sombra superior da barra")

    def test_bottom(self):
        self.assertEqual(self.obj.bottom, 0.0, "Sombra inferior da barra")

    def test_body_range(self):
        self.assertEqual(self.obj.body_range, 0.00006)

    def test_trend(self):
        self.assertEqual(self.obj.trend, "baixa")

    def test_volume(self):
        self.assertEqual(self.obj.volume, 25)

    def test_str(self):
        self.assertEqual(self.obj.__str__(), "-100 1.11575 1.11569 1.11569")

if __name__ == '__main__':
    unittest.main()

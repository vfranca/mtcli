#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from unittest import TestCase
from cli_trade.ema import *


class EmaTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
        self.times = 17

    def test_k(self):
        self.assertEqual(get_k(self.times), 0.111, "Coeficiente multiplicador da média móvel exponencial está errado para 17 períodos")

    def test_price_close(self):
        self.assertEqual(get_price_close(self.file), 92440.0, "Preço de fechamento atual errado")

    def test_last_ema(self):
        self.assertEqual(get_last_ema(self.times, self.file), 92441.18, "EMA anterior errada")

    def test_ema(self):
        self.assertEqual(get_ema(self.times, self.file), 92441.05, "EMA errada")

    def test_limit(self):
        self.assertEqual([1,2,3,4,5,6,7,8,9,10][-(3+1):-1], [7,8,9])

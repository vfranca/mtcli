#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from cli_trade.sma import *


class SmaTestCase(TestCase):

    def setUp(self):
        self.times = 17
        self.file = "tests/fixtures/var/wing19m5.csv"

    def test_sma(self):
        self.assertEqual(ma(self.times, self.file), 92440.0, "Retorna a média móvel simples de 17 períodos")

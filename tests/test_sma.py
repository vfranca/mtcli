#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from cli_trade.sma import *


class SmaTestCase(TestCase):

    def setUp(self):
        self.bars_qtt = 17
        self.file = "tests/fixtures/var/wing19m5.csv"

    def test_obtem_media_movel_aritmetica(self):
        self.assertEqual(ma(self.bars_qtt, self.file), 92440.29, "Retorna a média móvel simples de 17 períodos")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from cli_trade import indicator


class SmaTestCase(TestCase):

    def setUp(self):
        self.bars_qtt = 17
        self.file = "tests/fixtures/var/wing19m5.csv"

    def test_obtem_media_movel_aritmetica(self):
        self.assertEqual(indicator.sma.get_sma("win$n", "daily"), 104326.75)

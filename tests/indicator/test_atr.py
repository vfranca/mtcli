#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from unittest import TestCase
from cli_trade import indicator


class AtrTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"

    def test_obtem_o_atr_de_14_periodos(self):
        self.assertEqual(indicator.atr.get_atr("petr4", "h1", 14), 0.24)

    def test_limit(self):
        self.assertEqual([1, 2, 3, 4, 5][-2:], [4, 5])

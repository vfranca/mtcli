#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from unittest import TestCase
from cli_trade import atr


class AtrTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"

    def test_obtem_o_atr_de_14_periodos(self):
        self.assertEqual(atr.atr(self.file, 14), 237.14)

    def test_limit(self):
        self.assertEqual([1, 2, 3, 4, 5][-2:], [4, 5])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from cli_trade._view import *
from cli_trade._model import *
from cli_trade._bar import Bar
from cli_trade.conf import *


class ViewTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
        self.bars = bar_model(self.file)
        self.bar = Bar(self.bars[4])

    def test_obtem_view_com_padroes_brooks(self):
        self.assertEqual(brooks_view(self.bar, "ASC", 1, ""), "1 ASC  DOJI9R15.00  " + lbl_toptail + "50 83241.00 83081.00 83161.00 R160.00")

    def test_obtem_view_com_todos_os_dados(self):
        self.assertEqual(full_view(self.bar, "", ""), "  9 83146.00 83241.00 83081.00 83161.00 * 83161.00 83321.00")

    def test_obtem_view_de_canal(self):
        self.assertEqual(channel_view(self.bar, "ASC", 1), "1 ASC 83241.00 83081.00")

    def test_obtem_view_com_precos_de_fechamento(self):
        self.assertEqual(close_view(self.bar, 1), "1 83161.00")

    def test_obtem_view_com_maximas(self):
        self.assertEqual(high_view(self.bar, 1), "1 83241.00")

    def test_obtem_view_com_minimas(self):
        self.assertEqual(low_view(self.bar, 1), "1 83081.00")

    def test_obtem_view_com_volumes(self):
        self.assertEqual(volume_view(self.bar, "ASC", 1), "1 ASC alta 6794.00")

    def test_obtem_view_com_ranges(self):
        self.assertEqual(range_view(self.bar), "160.00")

    def test_obtem_view_com_numeros_de_fibonacci(self):
        self.assertEqual(fib_view(self.bar, "asc"), "asc 9 83142.12 83161.00 83179.88 * 83302.12 83321.00 83339.88")



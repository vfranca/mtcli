#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from cli_trade._view import *
from cli_trade._model import *
from cli_trade.lib.bar import Bar
from cli_trade.conf import *


class ViewTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
        self.bars = bar_model(self.file)
        self.bar = Bar(self.bars[4])

    def test_obtem_view_com_padroes_brooks(self):
        self.assertEqual(brooks_view(self.bar, "ASC", 1, ""), "1 ASC  DOJI9R15.00  " + lbl_toptail + "50 83241.00 83081.00 83161.00MP83161.00 R160.00")

    def test_obtem_view_com_o_padrao_ohlc(self):
        self.assertEqual(ohlc_view(self.bar), "2018.01.04 83146.00 83241.00 83081.00 83161.00 6794")

    def test_obtem_view_de_canal(self):
        self.assertEqual(channel_view(self.bar, "ASC", 1), "1 ASC 83241.00 83081.00")

    def test_obtem_view_com_precos_de_fechamento(self):
        self.assertEqual(close_view(self.bar, 1), "1 83161.00")

    def test_obtem_view_com_maximas(self):
        self.assertEqual(high_view(self.bar, 1), "1 83241.00")

    def test_obtem_view_com_minimas(self):
        self.assertEqual(low_view(self.bar, 1), "1 83081.00")

    def test_obtem_view_com_volumes(self):
        self.assertEqual(volume_view(self.bar, "ASC", 1), "1 ASC alta 6794")

    def test_obtem_view_com_ranges(self):
        self.assertEqual(range_view(self.bar, "ASC", 1), "1 ASC alta 160.00")




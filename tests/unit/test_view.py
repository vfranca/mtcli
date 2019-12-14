#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from chartcli import view
from chartcli import model
from chartcli.bar import Bar
from chartcli import conf


class ViewTestCase(unittest.TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
        self.bars = model.bar_model(self.file)
        self.bar = Bar(self.bars[4])

    def test_obtem_view_com_padroes_brooks(self):
        self.assertEqual(view.brooks_view(self.bar, "ASC", 1, "", 1.87), "1 ASC  DOJI9R15.00  " + conf.lbl_toptail + "50 83241.00 83081.00 83161.00MP83161.00 R160.00 1.87")

    def test_obtem_view_com_o_padrao_ohlc(self):
        self.assertEqual(view.ohlc_view(self.bar), "2018.01.04 83146.00 83241.00 83081.00 83161.00 6794")

    def test_obtem_view_de_canal(self):
        self.assertEqual(view.channel_view(self.bar, "ASC", 1), "1 ASC 83241.00 83081.00")

    def test_obtem_view_com_precos_de_fechamento(self):
        self.assertEqual(view.close_view(self.bar, 1), "1 83161.00")

    def test_obtem_view_com_maximas(self):
        self.assertEqual(view.high_view(self.bar, 1), "1 83241.00")

    def test_obtem_view_com_minimas(self):
        self.assertEqual(view.low_view(self.bar, 1), "1 83081.00")

    def test_obtem_view_com_volumes(self):
        self.assertEqual(view.volume_view(self.bar, "ASC", 1), "1 ASC VERDE 6794")

    def test_obtem_view_com_ranges(self):
        self.assertEqual(view.range_view(self.bar, "ASC", 1), "1 ASC VERDE 160.00")

    def test_obtem_view_com_variacao_percentual(self):
        self.assertEqual(view.var_view("ASC", 1.87, 1), "1 ASC 1.87")

if __name__ == '__main__':
    unittest.main()

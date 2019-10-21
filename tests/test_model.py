#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from cli_trade._model import *
from cli_trade._helper import *
from cli_trade._bar import Bar


class ModelTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
        self.bars = bar_model(self.file)
        self.bar = Bar(self.bars[4])

    def test_se_arquivo_csv_existe(self):
        self.assertTrue(bar_model(self.file))

    def test_filtro_por_data(self):
        bars = bar_model(self.file)
        bar = Bar(bars[0])
        self.assertEqual(bar.date, "2018.01.04")


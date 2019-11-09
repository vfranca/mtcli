#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from chartcli._model import *
from chartcli import _helper
from chartcli.lib.bar import Bar


class ModelTestCase(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()

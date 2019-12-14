#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, os
from chartcli.model import *
from chartcli import helper
from chartcli.bar import Bar


class ModelTestCase(unittest.TestCase):

    def setUp(self):
        fixtures_path = os.path.join(os.path.abspath('.'), 'tests', 'fixtures', 'var')
        self.file = os.path.join(fixtures_path, 'wing19m5.csv')
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

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from chartcli import _helper
from chartcli.lib.bar import Bar


class HelperTestCase(unittest.TestCase):
    """Tests for `chartcli` package."""

    def setUp(self):
        self.bar = Bar([
            '2015.04.01',
            '51187.00000',
            '56965.00000',
            '51187.00000',
            '56229.00000',
            '14628859',
            '8158109400'
        ])

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_calcula_o_ponto_medio_da_barra(self):
        self.assertEqual(_helper.get_medium_point(self.bar), 54076.00)

    def test_calcula_variacao_percentual_de_duas_barras(self):
        self.assertEqual(_helper.get_var(104300, 106250), 1.87)

if __name__ == '__main__':
    unittest.main()

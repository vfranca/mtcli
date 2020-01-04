#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import unittest
from mtcli import indicator


@unittest.skip("É necessário desacoplar constantes de configuração")
class AtrTestCase(unittest.TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"

    def test_obtem_o_atr_de_14_periodos(self):
        self.assertEqual(indicator.atr.get_atr("petr4", "h1", 14), 0.24)

    def test_limit(self):
        self.assertEqual([1, 2, 3, 4, 5][-2:], [4, 5])

if __name__ == '__main__':
    unittest.main()

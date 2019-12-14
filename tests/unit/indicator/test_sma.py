#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from chartcli import indicator


@unittest.skip("É necessário desacoplar constantes de configuração")
class SmaTestCase(unittest.TestCase):

    def setUp(self):
        self.bars_qtt = 17
        self.file = "tests/fixtures/var/wing19m5.csv"

    def test_obtem_media_movel_aritmetica(self):
        self.assertEqual(indicator.sma.get_sma("win$n", "daily"), 104326.75)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from mtcli.bar import Bar


class BarTestCase(unittest.TestCase):

    def setUp(self):
        self.obj = Bar([
            '2015.04.01',
            '51187.00000',
            '56965.00000',
            '51187.00000',
            '56229.00000',
            '14628859',
            '8158109400'
        ])

    def test_obtem_preco_abertura(self):
        self.assertEqual(self.obj.open, 51187.0)

    def test_obtem_preco_fechamento(self):
        self.assertEqual(self.obj.close, 56229.0)

    def test_obtem_maxima(self):
        self.assertEqual(self.obj.high, 56965.0)

    def test_obtem_minima(self):
        self.assertEqual(self.obj.low, 51187.0)

    def test_obtem_data(self):
        self.assertEqual(self.obj.date, "2015.04.01")

    def test_obtem_range_da_barra(self):
        self.assertEqual(self.obj.range, 5778)

    def test_obtem_range_do_corpo(self):
        self.assertEqual(self.obj.body_range, 5042)

    def test_obtem_tamanho_percentual_do_corpo(self):
        self.assertEqual(self.obj.body, 87)

    def test_obtem_tamanho_percentual_da_sombra_superior(self):
        self.assertEqual(self.obj.top, 13, "Sombra superior da barra")

    def test_obtem_tamanho_percentual_da_sombra_inferior(self):
        self.assertEqual(self.obj.bottom, 0, "Sombra inferior da barra")

    def test_obtem_tendencia_da_barra(self):
        self.assertEqual(self.obj.trend, "VERDE")

    def test_obtem_volume_da_barra(self):
        self.assertEqual(self.obj.volume, 14628859)

if __name__ == '__main__':
    unittest.main()

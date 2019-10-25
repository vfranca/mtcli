#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from unittest import TestCase
from cli_trade import ema


class EmaTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
        self.bars_qtt = 17

    def test_obtem_coeficiente_multiplicador(self):
        self.assertEqual(ema.get_k(self.bars_qtt), 0.111, "Coeficiente multiplicador da média móvel exponencial está errado para 17 períodos")

    def test_obtem_atual_preco_de_fechamento(self):
        self.assertEqual(ema.get_price_close(self.file), 92440.0, "Preço de fechamento atual errado")

    def test_obtem_ultima_media_movel_exponencial(self):
        self.assertEqual(ema.get_last_ema(self.bars_qtt, self.file), 92441.18, "EMA anterior errada")

    def test_ema(self):
        self.assertEqual(ema.get_ema(self.bars_qtt, self.file), 92441.05, "EMA errada")

    def test_limit(self):
        self.assertEqual([1,2,3,4,5,6,7,8,9,10][-(3+1):-1], [7,8,9])

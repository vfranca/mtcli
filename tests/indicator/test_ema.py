#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import unittest
from chartcli import indicator, conf


@unittest.skip("É necessário desacoplar constantes de configuração")
class EmaTest(unittest.TestCase):

    symbol = "win$n"
    period = "daily"
    count = 20

    def setUp(self):
        self.file = conf.csv_path + self.symbol + self.period + ".csv"

    def test_obtem_coeficiente_multiplicador(self):
        self.assertEqual(indicator.ema.get_k(self.count), 0.095)

    def test_obtem_atual_preco_de_fechamento(self):
        self.assertEqual(indicator.ema.get_price_close(self.file), 108080.0)

    def test_obtem_ultima_media_movel_exponencial(self):
        self.assertEqual(indicator.ema.get_last_ema(self.file, self.count), 104197.5)

    def test_ema(self):
        self.assertEqual(indicator.ema.get_ema(self.symbol, self.period, self.count), 104566.34)

    def test_limit(self):
        self.assertEqual([1,2,3,4,5,6,7,8,9,10][-(3+1):-1], [7,8,9])

if __name__ == '__main__':
    unittest.main()

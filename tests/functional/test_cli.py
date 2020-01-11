#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, mock
from click.testing import CliRunner
from mtcli import cli
from mtcli.conf import ORDER_REFUSED


class TestCli(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_exibe_o_padrao_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1"]
        )
        self.assertEqual(
            res.output, " ASC  DOJI7R0.02  TOP64 18.57 18.29 18.37MP18.43 R0.28 -0.38\n"
        )

    def test_exibe_o_canal_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "ch"]
        )
        self.assertEqual(res.output, " ASC 18.57 18.29\n")

    def test_exibe_o_fechamento_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "c"]
        )
        self.assertEqual(res.output, " 18.37\n")

    def test_exibe_a_maxima_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "h"]
        )
        self.assertEqual(res.output, " 18.57\n")

    def test_exibe_a_minima_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "l"]
        )
        self.assertEqual(res.output, " 18.29\n")

    def test_exibe_o_volume_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "vol"]
        )
        self.assertEqual(res.output, " ASC VERMELHO 16466\n")

    def test_exibe_o_range_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "r"]
        )
        self.assertEqual(res.output, " ASC VERMELHO 0.28\n")

    def test_exibe_a_variacao_percentual_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "var"]
        )
        self.assertEqual(res.output, " ASC -0.38\n")

    def test_exibe_o_atr_do_diario_da_abev3_de_14_periodos(self):
        res = self.runner.invoke(
            cli.atr, ["abev3", "--period", "daily", "--count", "14"]
        )
        self.assertEqual(res.output, "0.34\n")

    @mock.patch("mtcli.trading.mql5")
    def test_compra_a_mercado(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.Buy.return_value = 123456
        res = self.runner.invoke(
            cli.buy, ["abev3", "-v", 100, "-sl", 17.55, "-tp", 23.66]
        )
        self.assertEqual(res.output, "123456\n")

    @mock.patch("mtcli.trading.mql5")
    def test_falha_uma_compra_a_mercado(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.Buy.return_value = -1
        res = self.runner.invoke(
            cli.buy, ["abev3", "-v", 100, "-sl", 17.55, "-tp", 23.66]
        )
        self.assertEqual(res.output, ORDER_REFUSED + "\n")

    @mock.patch("mtcli.trading.mql5")
    def test_vende_a_mercado(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.Sell.return_value = 123456
        res = self.runner.invoke(
            cli.sell, ["abev3", "-v", 100, "-sl", 20.55, "-tp", 13.66]
        )
        self.assertEqual(res.output, "123456\n")

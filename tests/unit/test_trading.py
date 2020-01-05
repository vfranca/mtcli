#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
from mtcli import trading


class TestTrading(unittest.TestCase):
    """Testes para o módulo trading."""

    @patch("mtcli.trading.mql5")
    def test_obtem_o_preco_de_fechamento_do_ativo(self, mql5_mock):
        mql5_mock.iClose.return_value = 30.43
        self.assertEqual(trading.get_close("PETR4"), 30.43)

    @patch("mtcli.trading.mql5")
    def test_executa_uma_ordem_de_compra_a_mercado(self, mql5):
        mql5.Buy.return_value = 123456
        self.assertEqual(trading.buy("PETR4"), 123456)

    @patch("mtcli.trading.mql5")
    def test_executa_uma_ordem_de_compra_limitada(self, mql5):
        mql5.BuyLimit.return_value = 123456
        self.assertEqual(trading.buy_limit("PETR4", 29.00), 123456)

    @patch("mtcli.trading.mql5")
    def test_executa_uma_ordem_de_compra_stop(self, mql5):
        mql5.BuyStop.return_value = 123456
        self.assertEqual(trading.buy_stop("PETR4", 30.35), 123456)

    @patch("mtcli.trading.mql5")
    def test_executa_uma_ordem_de_venda_a_mercado(self, mql5):
        mql5.Sell.return_value = 123456
        self.assertEqual(trading.sell("PETR4"), 123456)

    @patch("mtcli.trading.mql5")
    def test_executa_uma_ordem_de_venda_limitada(self, mql5):
        mql5.SellLimit.return_value = 123456
        self.assertEqual(trading.sell_limit("petr4", 30.43), 123456)

    @patch("mtcli.trading.mql5")
    def test_executa_uma_ordem_de_venda_stop(self, mql5):
        mql5.SellStop.return_value = 123456
        self.assertEqual(trading.sell_stop("petr4", 30.80), 123456)

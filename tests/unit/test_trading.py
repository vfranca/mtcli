#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest.mock import patch
from mtcli import trading
from mtcli.conf import ORDER_REFUSED, CONNECTION_MISSING


class TestTrading(TestCase):
    """Testes para o módulo trading."""

    @patch("mtcli.trading.mql5")
    def test_obtem_o_preco_de_fechamento_do_ativo(self, mql5):
        mql5.iClose.return_value = 30.43
        self.assertEqual(trading.get_close("PETR4"), 30.43)

    @patch("mtcli.trading.mql5")
    def test_chama_uma_compra_a_mercado(self, mql5):
        mql5.Buy.return_value = 123456
        self.assertEqual(trading.buy("PETR4"), 123456)

    @patch("mtcli.trading.mql5")
    def test_falha_uma_chamada_de_compra_a_mercado(self, mql5):
        mql5.Buy.return_value = -1
        self.assertEqual(trading.buy("PETR4"), ORDER_REFUSED)

    @patch("mtcli.trading.mql5")
    def test_chamada_de_compra_limitada(self, mql5):
        mql5.BuyLimit.return_value = 123456
        self.assertEqual(trading.buy_limit("PETR4", 29.00), 123456)

    @patch("mtcli.trading.mql5")
    def test_falha_de_chamada_de_compra_limitada(self, mql5):
        mql5.BuyLimit.return_value = -1
        self.assertEqual(trading.buy_limit("PETR4", 29.00), ORDER_REFUSED)

    @patch("mtcli.trading.mql5")
    def test_chama_uma_compra_stop(self, mql5):
        mql5.BuyStop.return_value = 123456
        self.assertEqual(trading.buy_stop("PETR4", 30.35), 123456)

    @patch("mtcli.trading.mql5")
    def test_falha_uma_chamada_de_compra_stop(self, mql5):
        mql5.BuyStop.return_value = -1
        self.assertEqual(trading.buy_stop("PETR4", 30.35), ORDER_REFUSED)

    @patch("mtcli.trading.mql5")
    def test_chama_uma_venda_a_mercado(self, mql5):
        mql5.Sell.return_value = 123456
        self.assertEqual(trading.sell("PETR4"), 123456)

    @patch("mtcli.trading.mql5")
    def test_falha_uma_chamada_de_venda_a_mercado(self, mql5):
        mql5.Sell.return_value = -1
        self.assertEqual(trading.sell("PETR4"), ORDER_REFUSED)

    @patch("mtcli.trading.mql5")
    def test_chama_uma_venda_limitada(self, mql5):
        mql5.SellLimit.return_value = 123456
        self.assertEqual(trading.sell_limit("petr4", 30.43), 123456)

    @patch("mtcli.trading.mql5")
    def test_falha_uma_chamada_de_venda_limitada(self, mql5):
        mql5.SellLimit.return_value = -1
        self.assertEqual(trading.sell_limit("petr4", 30.43), ORDER_REFUSED)

    @patch("mtcli.trading.mql5")
    def test_chama_uma_venda_stop(self, mql5):
        mql5.SellStop.return_value = 123456
        self.assertEqual(trading.sell_stop("petr4", 30.80), 123456)

    @patch("mtcli.trading.mql5")
    def test_falha_uma_chamada_de_venda_stop(self, mql5):
        mql5.SellStop.return_value = -1
        self.assertEqual(trading.sell_stop("petr4", 30.80), ORDER_REFUSED)

    @patch("mtcli.trading.mql5")
    def test_consulta_total_de_ordens_pendentes(self, mql5):
        mql5.OrdersTotal.return_value =3
        self.assertEqual(trading.get_total_orders(), 3)

    @patch("mtcli.trading.mql5")
    def test_lista_ordens_pendentes(self, mql5):
        mql5.OrderAll.return_value = [{
            "TICKET": 273443559,
            "TIME_SETUP": "1578489931",
            "TYPE": "ORDER_TYPE_BUY_LIMIT",
            "STATE": "ORDER_STATE_PLACED",
            "TIME_EXPIRATION": "2020.01.08 00:00:00",
            "TIME_DONE": "1970.01.01 00:00:00",
            "TIME_SETUP_MSC": 1578489931129,
            "TIME_DONE_MSC": 0,
            "TYPE_FILLING": "TYPE_FILLING_RETURN",
            "TYPE_TIME": "TYPE_TIME_DAY",
            "MAGIC": 0,
            "POSITION_ID": 0,
            "POSITION_BY_ID": 0,
            "VOLUME_INITIAL": 1.0,
            "VOLUME_CURRENT": 1.0,
            "PRICE_OPEN": 116500.0,
            "SL": 116300.0,
            "TP": 116900.0,
            "PRICE_CURRENT": 117110.0,
            "PRICE_STOPLIMIT": 0.0,
            "SYMBOL": "WING20",
            "COMMENT": ""
        }]
        self.assertEqual(trading.get_orders(), "273443559 ORDER_TYPE_BUY_LIMIT WING20 1.0 116500.0 116300.0 116900.0\n")

    @patch("mtcli.trading.mql5")
    def test_lista_ordens_pendentes_sem_conexao_com_metatrader(self, mql5):
        mql5.OrderAll.return_value = None
        self.assertEqual(trading.get_orders(), CONNECTION_MISSING)

    @patch("mtcli.trading.mql5")
    def test_cancela_todas_as_ordens_pendentes(self, mql5):
        mql5.CancelAllOrder.return_value = 1
        self.assertTrue(trading.cancel_orders())

    @patch("mtcli.trading.mql5")
    def test_falha_o_cancelamento_de_todas_as_ordens_pendentes(self, mql5):
        mql5.CancelAllOrder.return_value = 0
        self.assertFalse(trading.cancel_orders())

    @patch("mtcli.trading.mql5")
    def test_cancela_uma_ordem_pendente_pelo_ticket(self, mql5):
        mql5.DeleteOrder.return_value = 1
        self.assertTrue(trading.cancel_order(1234567890))

    @patch("mtcli.trading.mql5")
    def test_falha_o_cancelamento_de_uma_ordem_pendente_pelo_ticket(self, mql5):
        mql5.DeleteOrder.return_value = 0
        self.assertFalse(trading.cancel_order(1234567890))

    @patch("mtcli.trading.mql5")
    def test_obtem_total_de_posicoes_abertas(self, mql5):
        mql5.PositionsTotal.return_value = 6
        self.assertEqual(trading.get_total_positions(), 6)

    @patch("mtcli.trading.mql5")
    def test_obtem_lista_de_posicoes_abertas(self, mql5):
        mql5.PositionAll.return_value = [{
            "TICKET": 272337225,
            "SYMBOL": "WING20",
            "TYPE": "POSITION_TYPE_BUY",
            "VOLUME": 1.0,
            "PRICE_OPEN": 117360.0,
            "SL": 117110.0,
            "TP": 117860.0,
            "PRICE_CURRENT": 117360.0,
            "TIME": "2020-01-06 21:45:39"
        }]
        self.assertEqual(trading.get_positions(), "272337225 WING20 POSITION_TYPE_BUY 1.0 117360.0 117110.0 117860.0 117360.0 2020-01-06 21:45:39\n")


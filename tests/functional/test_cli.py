#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, mock
from click.testing import CliRunner
from mtcli import cli
from mtcli.conf import ORDER_REFUSED, PRICE_CURRENT_ERROR, POSITION_MODIFIED_SUCCESS


class TestCli(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.positions = [
            {
                "TICKET": 272337225,
                "SYMBOL": "WING20",
                "TYPE": "POSITION_TYPE_BUY",
                "VOLUME": 1.0,
                "PRICE_OPEN": 117360.0,
                "SL": 117110.0,
                "TP": 117860.0,
                "PRICE_CURRENT": 117360.0,
                "TIME": "2020-01-06 21:45:39",
            }
        ]

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

    @mock.patch("mtcli.trading.mql5")
    def test_falha_uma_venda_a_mercado(self, mql5):
        mql5.Sell.return_value = -1
        res = self.runner.invoke(
            cli.sell, ["abev3", "-v", 100, "-sl", 20.50, "-tp", 13.50]
        )
        self.assertEqual(res.output, ORDER_REFUSED + "\n")

    @mock.patch("mtcli.trading.mql5")
    def test_lista_ordens_pendentes(self, mql5):
        mql5.OrderAll.return_value = [
            {
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
                "COMMENT": "",
            }
        ]
        res = self.runner.invoke(cli.orders)
        self.assertEqual(
            res.output,
            "273443559 ORDER_TYPE_BUY_LIMIT WING20 1.0 116500.0 116300.0 116900.0\n\n",
        )

    @mock.patch("mtcli.trading.mql5")
    def test_lista_posicoes_abertas(self, mql5):
        mql5.PositionAll.return_value = self.positions
        res = self.runner.invoke(cli.positions)
        self.assertEqual(
            res.output,
            "272337225 WING20 POSITION_TYPE_BUY 1.0 117360.0 117110.0 117860.0 117360.0 2020-01-06 21:45:39\n\n",
        )

    @mock.patch("mtcli.trading.mql5")
    def test_cancela_todas_as_posicoes_e_ordens(self, mql5):
        mql5.CancelAllOrder.return_value = 1
        mql5.CancelAllPosition.return_value = 1
        res = self.runner.invoke(cli.cancel, ["all"])
        self.assertEqual(
            res.output,
            "Todas as órdens foram canceladas com sucesso!\nTodas as posições foram canceladas com sucesso!\n",
        )

    @mock.patch("mtcli.trading.mql5")
    def test_cancela_todas_as_ordens_pendentes(self, mql5):
        mql5.CancelAllOrder.return_value = 1
        res = self.runner.invoke(cli.cancel, ["orders"])
        self.assertEqual(res.output, "Todas as órdens foram canceladas com sucesso!\n")

    @mock.patch("mtcli.trading.mql5")
    def test_altera_o_stoploss_de_uma_posicao_pelo_ativo(self, mql5):
        mql5.PositionAll.return_value = self.positions
        mql5.PositionModifySymbol.return_value = 1
        res = self.runner.invoke(cli.positions, ["-s", "WING20", "-sl", 116500.0])
        self.assertEqual(res.output, POSITION_MODIFIED_SUCCESS + "\n")

    @mock.patch("mtcli.trading.mql5")
    def test_altera_o_take_profit_de_uma_posicao_pelo_ativo(self, mql5):
        mql5.PositionAll.return_value = self.positions
        mql5.PositionModifySymbol.return_value = 1
        res = self.runner.invoke(cli.positions, ["-s", "WING20", "-tp", 117500.0])
        self.assertEqual(res.output, POSITION_MODIFIED_SUCCESS + "\n")

    @mock.patch("mtcli.trading.mql5")
    def test_venda_stop_com_preco_fechamento_none(self, mql5):
        mql5.iClose.return_value = None
        mql5.SellStop.return_value = 123456
        res = self.runner.invoke(
            cli.sell, ["wing20", "-p", 116110, "-v", 1, "-sl", 116450, "-tp", 115790]
        )
        self.assertEqual(res.output, PRICE_CURRENT_ERROR + "\n")

    @mock.patch("mtcli.trading.mql5")
    def test_altera_stoploss_de_umaposicao_com_minuscula(self, mql5):
        mql5.PositionAll.return_value = self.positions
        res = self.runner.invoke(cli.positions, ["-s", "wing20", "-sl", 115200])
        self.assertEqual(res.output, POSITION_MODIFIED_SUCCESS + "\n")

    @mock.patch("mtcli.trading.mql5")
    def test_altera_takeprofit_de_umaposicao_com_minuscula(self, mql5):
        mql5.PositionAll.return_value = self.positions
        res = self.runner.invoke(cli.positions, ["-s", "wing20", "-tp", 118200])
        self.assertEqual(res.output, POSITION_MODIFIED_SUCCESS + "\n")

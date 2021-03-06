from unittest import TestCase, mock
from click.testing import CliRunner
from mtcli import cli
from mtcli.conf import (
    ORDER_ERROR,
    PRICE_CURRENT_ERROR,
    POSITION_MODIFIED_SUCCESS,
    ORDER_CANCELED_ERROR,
    ORDER_CANCELED_SUCCESS,
    POSITION_CANCELED_ERROR,
    POSITION_CANCELED_SUCCESS,
)


class TestCli(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.account = [
            {
                "LOGIN": 1090113038,
                "TRADE_MODE": "ACCOUNT_TRADE_MODE_DEMO",
                "LEVERAGE": "1",
                "LIMIT_ORDERS": 0,
                "MARGIN_SO_MODE": "ACCOUNT_STOPOUT_MODE_MONEY",
                "TRADE_ALLOWED": "1",
                "TRADE_EXPERT": "1",
                "MARGIN_MODE": "ACCOUNT_MARGIN_MODE_RETAIL_NETTING",
                "CURRENCY_DIGITS": "2",
                "BALANCE": 101010.99,
                "CREDIT": 0.0,
                "PROFIT": 0.0,
                "EQUITY": 101010.99,
                "MARGIN": 0.0,
                "MARGIN_FREE": 101010.99,
                "MARGIN_LEVEL": 0.0,
                "MARGIN_SO_CALL": 0.0,
                "MARGIN_INITIAL": 0.0,
                "MARGIN_MAINTENANCE": 0.0,
                "ASSETS": 0.0,
                "LIABILITIES": 0.0,
                "COMMISSION_BLOCKED": 0.0,
                "NAME": "VALMIR FRANCA DA SILVA",
                "SERVER": "CLEAR-Demo",
                "CURRENCY": "BRL",
                "COMPANY": "CLEAR CTVM S.A.",
            }
        ]
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
        self.assertEqual(res.exit_code, 0)

    def test_exibe_o_canal_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "ch"]
        )
        self.assertEqual(res.output, " ASC 18.57 18.29\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_o_fechamento_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "c"]
        )
        self.assertEqual(res.output, " 18.37\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_a_maxima_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "h"]
        )
        self.assertEqual(res.output, " 18.57\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_a_minima_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "l"]
        )
        self.assertEqual(res.output, " 18.29\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_o_volume_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "vol"]
        )
        self.assertEqual(res.output, " ASC VERMELHO 16466\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_o_range_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "r"]
        )
        self.assertEqual(res.output, " ASC VERMELHO 0.28\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_a_variacao_percentual_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            cli.bars, ["abev3", "--period", "daily", "--count", "1", "--view", "var"]
        )
        self.assertEqual(res.output, " ASC -0.38\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_o_atr_do_diario_da_abev3_de_14_periodos(self):
        res = self.runner.invoke(
            cli.atr, ["abev3", "--period", "daily", "--count", "14"]
        )
        self.assertEqual(res.output, "0.34\n")
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_compra_a_mercado(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.Buy.return_value = 123456
        res = self.runner.invoke(
            cli.buy, ["abev3", "-v", 100, "-sl", 17.55, "-tp", 23.66]
        )
        self.assertEqual(res.output, "123456\n")
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_compra_a_mercado(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.Buy.return_value = -1
        res = self.runner.invoke(
            cli.buy, ["abev3", "-v", 100, "-sl", 17.55, "-tp", 23.66]
        )
        self.assertEqual(res.output, ORDER_ERROR + "\n")
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_vende_a_mercado(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.Sell.return_value = 123456
        res = self.runner.invoke(
            cli.sell, ["abev3", "-v", 100, "-sl", 20.55, "-tp", 13.66]
        )
        self.assertEqual(res.output, "123456\n")
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_venda_a_mercado(self, mql5):
        mql5.Sell.return_value = -1
        res = self.runner.invoke(
            cli.sell, ["abev3", "-v", 100, "-sl", 20.50, "-tp", 13.50]
        )
        self.assertEqual(res.output, ORDER_ERROR + "\n")
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
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
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_lista_posicoes_abertas(self, mql5):
        mql5.PositionAll.return_value = self.positions
        res = self.runner.invoke(cli.positions)
        self.assertEqual(
            res.output,
            "272337225 WING20 POSITION_TYPE_BUY 1.0 117360.0 117110.0 117860.0 117360.0 2020-01-06 21:45:39\n\n",
        )
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_altera_o_stoploss_de_uma_posicao_pelo_ativo(self, mql5):
        mql5.PositionAll.return_value = self.positions
        mql5.PositionModifySymbol.return_value = 1
        res = self.runner.invoke(cli.positions, ["-s", "WING20", "-sl", 116500.0])
        self.assertEqual(res.output, POSITION_MODIFIED_SUCCESS + "\n")
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_altera_o_take_profit_de_uma_posicao_pelo_ativo(self, mql5):
        mql5.PositionAll.return_value = self.positions
        mql5.PositionModifySymbol.return_value = 1
        res = self.runner.invoke(cli.positions, ["-s", "WING20", "-tp", 117500.0])
        self.assertEqual(res.output, POSITION_MODIFIED_SUCCESS + "\n")
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_todas_as_posicoes_e_ordens(self, mql5):
        mql5.CancelAllOrder.return_value = 1
        mql5.CancelAllPosition.return_value = 1
        res = self.runner.invoke(cli.cancel, ["all"])
        self.assertEqual(
            res.output, ORDER_CANCELED_SUCCESS + "\n" + POSITION_CANCELED_SUCCESS + "\n"
        )
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_todas_as_ordens_pendentes(self, mql5):
        mql5.CancelAllOrder.return_value = 1
        res = self.runner.invoke(cli.cancel, ["orders"])
        self.assertEqual(res.output, ORDER_CANCELED_SUCCESS + "\n")
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_venda_stop_com_pymql5_retornando_none(self, mql5):
        mql5.iClose.return_value = 116310
        mql5.SellStop.return_value = None
        res = self.runner.invoke(
            cli.sell, ["wing20", "-p", 116110, "-v", 1, "-sl", 0, "-tp", 0]
        )
        self.assertEqual(res.output, "")
        self.assertEqual(res.exit_code, 1)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_altera_stoploss_de_umaposicao_com_minuscula(self, mql5):
        mql5.PositionAll.return_value = self.positions
        res = self.runner.invoke(cli.positions, ["-s", "wing20", "-sl", 115200])
        self.assertEqual(res.output, POSITION_MODIFIED_SUCCESS + "\n")
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_altera_takeprofit_de_umaposicao_com_minuscula(self, mql5):
        mql5.PositionAll.return_value = self.positions
        res = self.runner.invoke(cli.positions, ["-s", "wing20", "-tp", 118200])
        self.assertEqual(res.output, POSITION_MODIFIED_SUCCESS + "\n")
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_exibe_dados_da_conta_de_trading(self, mql5):
        mql5.AccountInfoAll.return_value = self.account
        res = self.runner.invoke(cli.account)
        self.assertEqual(
            res.output,
            "1090113038 ACCOUNT_TRADE_MODE_DEMO VALMIR FRANCA DA SILVA CLEAR-Demo CLEAR CTVM S.A.\n",
        )
        self.assertEqual(res.exit_code, 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_exibe_dados_da_conta_de_trading_sem_conexao_com_o_metatrader(self, mql5):
        mql5.AccountInfoAll.return_value = None
        res = self.runner.invoke(cli.account)
        self.assertEqual(res.exit_code, 1)

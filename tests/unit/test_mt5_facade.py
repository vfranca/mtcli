from unittest import TestCase, mock
from mtcli.mt5_facade import MT5Facade
from mtcli.conf import CONNECTION_ERROR


class TestMT5Facade(TestCase):
    def setUp(self):
        self.mt5 = MT5Facade("abev3", "daily")
        self.orders = [
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

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_pega_preco_de_fechamento(self, mql5):
        mql5.iClose.return_value = 18.50
        self.assertEqual(self.mt5.close(), 18.50)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_pega_preco_de_fechamento_sem_conexao_com_o_metatrader(self, mql5):
        mql5.iClose.return_value = None
        self.assertRaises(Exception, self.mt5.close)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_abre_uma_posicao_comprada_com_ordem_a_mercado(self, mql5):
        mql5.Buy.return_value = 123456
        self.assertEqual(self.mt5.buy(100), 123456)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_compra_a_mercado(self, mql5):
        mql5.Buy.return_value = -1
        self.assertEqual(self.mt5.buy(100), 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_compra_a_mercado_sem_conexao_com_o_metatrader(self, mql5):
        mql5.Buy.return_value = None
        self.assertRaises(Exception, self.mt5.buy)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_abre_uma_posicao_comprada_com_ordem_limit(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.BuyLimit.return_value = 123456
        self.assertEqual(self.mt5.buy_limit(100, 17.50), 123456)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_compra_limit(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.BuyLimit.return_value = -1
        self.assertEqual(self.mt5.buy_limit(100, 17.50), 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_compra_limit_sem_conexao_com_o_metatrader(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.BuyLimit.return_value = None
        self.assertRaises(Exception, self.mt5.buy_limit)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_abre_uma_posicao_comprada_com_ordem_stop(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.BuyStop.return_value = 123456
        self.assertEqual(self.mt5.buy_stop(100, 19.50), 123456)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_compra_stop(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.BuyStop.return_value = -1
        self.assertEqual(self.mt5.buy_stop(100, 19.50), 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_compra_stop_sem_conexao_com_o_metatrader(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.BuyStop.return_value = None
        self.assertRaises(Exception, self.mt5.buy_stop)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_abre_uma_posicao_vendida_com_ordem_a_mercado(self, mql5):
        mql5.Sell.return_value = 123456
        self.assertEqual(self.mt5.sell(100), 123456)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_venda_a_mercado(self, mql5):
        mql5.Sell.return_value = -1
        self.assertEqual(self.mt5.sell(100), 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_venda_a_mercado_sem_conexao_com_o_metatrader(self, mql5):
        mql5.Sell.return_value = None
        self.assertRaises(Exception, self.mt5.sell)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_abre_uma_posicao_vendida_com_ordem_limit(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.SellLimit.return_value = 123456
        self.assertEqual(self.mt5.sell_limit(100, 19.50), 123456)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_venda_limit(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.SellLimit.return_value = -1
        self.assertEqual(self.mt5.sell_limit(100, 19.50), 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_venda_limit_sem_conexao_com_o_metatrader(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.SellLimit.return_value = None
        self.assertRaises(Exception, self.mt5.sell_limit, 100, 19.50)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_abre_uma_posicao_vendida_com_ordem_stop(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.SellStop.return_value = 123456
        self.assertEqual(self.mt5.sell_stop(100, 17.50), 123456)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_venda_stop(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.SellStop.return_value = -1
        self.assertEqual(self.mt5.sell_stop(100, 17.50), 0)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_uma_venda_stop_sem_conexao_com_o_metatrader(self, mql5):
        mql5.iClose.return_value = 18.50
        mql5.SellStop.return_value = None
        self.assertRaises(Exception, self.mt5.sell_stop, 100, 17.50)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_lista_todas_as_ordens_pendentes(self, mql5):
        mql5.OrderAll.return_value = self.orders
        self.assertEqual(
            self.mt5.orders(),
            "273443559 ORDER_TYPE_BUY_LIMIT WING20 1.0 116500.0 116300.0 116900.0\n",
        )

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_lista_todas_as_ordens_pendentes_sem_conexao_com_o_metatrader(
        self, mql5
    ):
        mql5.OrderAll.return_value = None
        self.assertRaises(Exception, self.mt5.orders)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_todas_as_ordens_pendentes(self, mql5):
        mql5.CancelAllOrder.return_value = 1
        self.assertTrue(self.mt5.cancel_orders())

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_o_cancelamento_de_todas_as_ordens_pendentes(self, mql5):
        mql5.CancelAllOrder.return_value = 0
        self.assertFalse(self.mt5.cancel_orders())

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_todas_as_ordens_pendentes_sem_conexao_com_o_metatrader(self, mql5):
        mql5.CancelAllOrder.return_value = None
        self.assertRaises(Exception, self.mt5.cancel_orders)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_uma_ordem_pendente_pelo_ticket(self, mql5):
        mql5.DeleteOrder.return_value = 1
        self.assertTrue(self.mt5.cancel_order(1234567890))

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_o_cancelamento_de_uma_ordem_pendente_pelo_ticket(self, mql5):
        mql5.DeleteOrder.return_value = 0
        self.assertFalse(self.mt5.cancel_order(1234567890))

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_uma_ordem_pendente_pelo_ticket_sem_conexao_com_o_metatrader(
        self, mql5
    ):
        mql5.DeleteOrder.return_value = None
        self.assertRaises(Exception, self.mt5.cancel_order, 1234567890)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_lista_todas_as_posicoes_abertas(self, mql5):
        mql5.PositionAll.return_value = self.positions
        self.assertEqual(
            self.mt5.positions(),
            "272337225 WING20 POSITION_TYPE_BUY 1.0 117360.0 117110.0 117860.0 117360.0 2020-01-06 21:45:39\n",
        )

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_lista_todas_as_posicoes_abertas_sem_conexao_com_o_metatrader(self, mql5):
        mql5.PositionAll.return_value = None
        self.assertRaises(Exception, self.mt5.positions)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_altera_o_stoploss_de_uma_posicao_pelo_ativo(self, mql5):
        mql5.PositionAll.return_value = self.positions
        mql5.PositionModifySymbol.return_value = 1
        self.assertTrue(self.mt5.modify_position_symbol("wing20", 116500.0, 0.0))

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_altera_o_takeprofit_de_uma_posicao_pelo_ativo(self, mql5):
        mql5.PositionAll.return_value = self.positions
        mql5.PositionModifySymbol.return_value = 1
        self.assertTrue(self.mt5.modify_position_symbol("wing20", 0.0, 117500.0))

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_alteracao_do_takeprofit_de_uma_posicao_pelo_ativo(self, mql5):
        mql5.PositionAll.return_value = self.positions
        mql5.PositionModifySymbol.return_value = 0
        self.assertFalse(self.mt5.modify_position_symbol("wing20", 0.0, 117500.0))

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_altera_o_takeprofit_de_uma_posicao_pelo_ativo_sem_conexao_com_o_metatrader(
        self, mql5
    ):
        mql5.PositionAll.return_value = self.positions
        mql5.PositionModifySymbol.return_value = None
        self.assertRaises(
            Exception, self.mt5.modify_position_symbol, "wing20", 0.0, 117500.0
        )

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_todas_as_posicoes_abertas(self, mql5):
        mql5.CancelAllPosition.return_value = 1
        self.assertTrue(self.mt5.cancel_positions())

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_o_cancelamento_de_todas_as_posicoes_abertas(self, mql5):
        mql5.CancelAllPosition.return_value = 0
        self.assertFalse(self.mt5.cancel_positions())

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_todas_as_posicoes_abertas_sem_conexao_com_o_metatrader(self, mql5):
        mql5.CancelAllPosition.return_value = None
        self.assertRaises(Exception, self.mt5.cancel_positions)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_uma_posicao_pelo_ativo(self, mql5):
        mql5.PositionCloseSymbol.return_value = 1
        self.assertTrue(self.mt5.cancel_position_symbol("abev3"))

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_o_cancelamento_de_uma_posicao_pelo_ativo(self, mql5):
        mql5.PositionCloseSymbol.return_value = 0
        self.assertFalse(self.mt5.cancel_position_symbol("abev3"))

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_uma_posicao_pelo_ativo_sem_conexao_com_o_metatrader(self, mql5):
        mql5.PositionCloseSymbol.return_value = None
        self.assertRaises(Exception, self.mt5.cancel_position_symbol, "abev3")

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_uma_posicao_pelo_ticket(self, mql5):
        mql5.PositionCloseTicket.return_value = 1
        self.assertTrue(self.mt5.cancel_position_ticket(1234567890))

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_falha_o_cancelamento_de_uma_posicao_pelo_ticket(self, mql5):
        mql5.PositionCloseTicket.return_value = 0
        self.assertFalse(self.mt5.cancel_position_ticket(1234567890))

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_cancela_uma_posicao_pelo_ticket_sem_conexao_com_o_metatrader(self, mql5):
        mql5.PositionCloseTicket.return_value = None
        self.assertRaises(Exception, self.mt5.cancel_position_ticket, 1234567890)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_pega_informacoes_da_conta_de_negociacao(self, mql5):
        mql5.AccountInfoAll.return_value = [
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
        self.assertEqual(
            self.mt5.account(),
            "1090113038 ACCOUNT_TRADE_MODE_DEMO VALMIR FRANCA DA SILVA CLEAR-Demo CLEAR CTVM S.A.",
        )

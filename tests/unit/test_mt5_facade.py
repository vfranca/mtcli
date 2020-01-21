from unittest import TestCase, mock
from mtcli.mt5_facade import MT5Facade
from mtcli.conf import CONNECTION_ERROR


class TestMT5Facade(TestCase):
    def setUp(self):
        self.mt5 = MT5Facade("abev3", "daily")
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

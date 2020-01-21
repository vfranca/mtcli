from unittest import TestCase, mock
from mtcli.mt5_facade import MT5Facade
from mtcli.conf import CONNECTION_ERROR


class TestMT5Facade(TestCase):
    def setUp(self):
        self.mt5 = MT5Facade("abev3", "daily")

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_pega_preco_de_fechamento(self, mql5):
        mql5.iClose.return_value = 18.50
        self.assertEqual(self.mt5.close(), 18.50)

    @mock.patch("mtcli.mt5_facade.mql5")
    def test_pega_preco_de_fechamento_sem_conexao_com_o_metatrader(self, mql5):
        mql5.iClose.return_value = None
        self.assertRaises(Exception, self.mt5.close)

from unittest import TestCase, mock, skip
from mtcli import indicator, conf


class TestEma(TestCase):

    symbol = "ABEV3"
    period = "Daily"
    count = 20

    def setUp(self):
        self.file = conf.csv_path + self.symbol + self.period + ".csv"

    @mock.patch("mtcli.indicator.ema.conf")
    def test_obtem_coeficiente_multiplicador(self, conf):
        conf.csv_path.return_value = (
            "C:/Users/Administrador/python/mtcli/tests/fixtures/Files/"
        )
        self.assertEqual(indicator.ema.get_k(self.count), 0.095)

    @mock.patch("mtcli.indicator.ema.conf")
    def test_obtem_atual_preco_de_fechamento(self, conf):
        conf.csv_path.return_value = (
            "C:/Users/Administrador/python/mtcli/tests/fixtures/Files/"
        )
        self.assertEqual(indicator.ema.get_price_close(self.file), 18.37)

    @mock.patch("mtcli.indicator.ema.conf")
    def test_obtem_ultima_media_movel_exponencial(self, conf):
        conf.csv_path.return_value = (
            "C:/Users/Administrador/python/mtcli/tests/fixtures/Files/"
        )
        self.assertEqual(indicator.ema.get_last_ema(self.file, self.count), 17.9)

    @skip("")
    @mock.patch("mtcli.indicator.ema.conf")
    def test_ema(self, conf):
        conf.csv_path.return_value = (
            "C:/Users/Administrador/python/mtcli/tests/fixtures/Files/"
        )
        self.assertEqual(
            indicator.ema.get_ema(self.symbol, self.period, self.count), 104566.34
        )

    def test_limit(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10][-(3 + 1) : -1], [7, 8, 9])


if __name__ == "__main__":
    unittest.main()

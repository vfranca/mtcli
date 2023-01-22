# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import unittest, os
from mtcli import views as view, conf
from mtcli.csv_data import get_data
from mtcli.pa.pa_bar import Bar


class TestUnitViews(unittest.TestCase):
    def setUp(self):
        self.file = os.path.join(
            os.path.abspath("."), "tests", "fixtures", "files", "ABEV3D1.csv"
        )
        self.rates = get_data(self.file)
        self.bar = Bar(self.rates[4])

    def test_obtem_view_com_padroes_de_price_action(self):
        self.assertEqual(
            view.brooks_view(self.bar, "ASC", 1, "", 1.87),
            "1 ASC  VERMELHO20R0.05  BOTTOM56 17.59 17.34 17.48MP17.46 R0.25 1.87",
        )

    def test_obtem_view_com_o_padrao_ohlc(self):
        self.assertEqual(
            view.ohlc_view(self.bar), "2017.06.29 17.53 17.59 17.34 17.48 14436"
        )

    def test_obtem_view_de_grafico_minimo(self):
        self.assertEqual(view.channel_view(self.bar, "ASC", 1), "1 ASC 17.59 17.34")

    def test_obtem_view_com_fechamentos(self):
        self.assertEqual(view.close_view(self.bar, 1), "1 17.48")

    def test_obtem_view_com_maximas(self):
        self.assertEqual(view.high_view(self.bar, 1), "1 17.59")

    def test_obtem_view_com_minimas(self):
        self.assertEqual(view.low_view(self.bar, 1), "1 17.34")

    def test_obtem_view_com_volumes(self):
        self.assertEqual(view.volume_view(self.bar, "ASC", 1), "1 ASC VERMELHO 14436")

    def test_obtem_view_com_ranges(self):
        self.assertEqual(view.range_view(self.bar, "ASC", 1), "1 ASC VERMELHO 0.25")

    def test_obtem_view_com_variacao_percentual(self):
        self.assertEqual(view.var_view("ASC", 1.87, 1), "1 ASC 1.87")


if __name__ == "__main__":
    unittest.main()

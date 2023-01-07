# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import unittest
from mtcli.pa import helpers as helper
from mtcli.pa.pa_bar import Bar


class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(
            [
                "2015.04.01",
                "51187.00000",
                "56965.00000",
                "51187.00000",
                "56229.00000",
                "14628859",
                "8158109400",
            ]
        )

    def tearDown(self):
        pass

    def test_calcula_o_ponto_medio_da_barra(self):
        self.assertEqual(helper.get_medium_point(self.bar), 54076.00)

    def test_calcula_variacao_percentual_de_duas_barras(self):
        self.assertEqual(helper.get_var(104300, 106250), 1.87)


if __name__ == "__main__":
    unittest.main()

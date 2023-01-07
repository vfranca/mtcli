# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
from unittest import TestCase, mock, skip
from click.testing import CliRunner
from mtcli.mt import mt


class TestBars(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_exibe_o_grafico_completo_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            mt, ["bars", "abev3", "--period", "d1", "--count", "1"]
        )
        self.assertEqual(
            res.output, " ASC  DOJI7R0.02  TOP64 18.57 18.29 18.37MP18.43 R0.28 -0.38\n"
        )
        self.assertEqual(res.exit_code, 0)

    def test_exibe_o_grafico_minimo_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "ch"]
        )
        self.assertEqual(res.output, " ASC 18.57 18.29\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_o_grafico_de_fechamentos_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "c"]
        )
        self.assertEqual(res.output, " 18.37\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_o_grafico_de_maximas_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "h"]
        )
        self.assertEqual(res.output, " 18.57\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_o_grafico_de_minimas_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "l"]
        )
        self.assertEqual(res.output, " 18.29\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_o_grafico_de_volume_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "vol"]
        )
        self.assertEqual(res.output, " ASC VERMELHO 16466\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_grafico_de_ranges_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "r"]
        )
        self.assertEqual(res.output, " ASC VERMELHO 0.28\n")
        self.assertEqual(res.exit_code, 0)

    def test_exibe_o_grafico_de_variacao_percentual_da_ultima_barra_do_diario(self):
        res = self.runner.invoke(
            mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "var"]
        )
        self.assertEqual(res.output, " ASC -0.38\n")
        self.assertEqual(res.exit_code, 0)

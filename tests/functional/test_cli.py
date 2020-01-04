#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from click.testing import CliRunner
from mtcli import cli


class TestCli(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_exibe_o_padrao_da_ultima_barra_do_diario(self):
        run = self.runner.invoke(cli.bars, ['abev3', '--period', 'daily', '--count', '1'])
        self.assertEqual(run.output, " ASC  DOJI7R0.02  TOP64 18.57 18.29 18.37MP18.43 R0.28 -0.38\n")

    def test_exibe_o_canal_da_ultima_barra_do_diario(self):
        run = self.runner.invoke(cli.bars, ['abev3', '--period', 'daily', '--count', '1', '--view', 'ch'])
        self.assertEqual(run.output, " ASC 18.57 18.29\n")

    def test_exibe_o_fechamento_da_ultima_barra_do_diario(self):
        run = self.runner.invoke(cli.bars, ['abev3', '--period', 'daily', '--count', '1', '--view', 'c'])
        self.assertEqual(run.output, " 18.37\n")

    def test_exibe_a_maxima_da_ultima_barra_do_diario(self):
        run = self.runner.invoke(cli.bars, ['abev3', '--period', 'daily', '--count', '1', '--view', 'h'])
        self.assertEqual(run.output, " 18.57\n")

    def test_exibe_a_minima_da_ultima_barra_do_diario(self):
        run = self.runner.invoke(cli.bars, ['abev3', '--period', 'daily', '--count', '1', '--view', 'l'])
        self.assertEqual(run.output, " 18.29\n")

    def test_exibe_o_volume_da_ultima_barra_do_diario(self):
        run = self.runner.invoke(cli.bars, ['abev3', '--period', 'daily', '--count', '1', '--view', 'vol'])
        self.assertEqual(run.output, ' ASC VERMELHO 16466\n')

    def test_exibe_o_range_da_ultima_barra_do_diario(self):
        run = self.runner.invoke(cli.bars, ['abev3', '--period', 'daily', '--count', '1', '--view', 'r'])
        self.assertEqual(run.output, ' ASC VERMELHO 0.28\n')

    def test_exibe_a_variacao_percentual_da_ultima_barra_do_diario(self):
        run = self.runner.invoke(cli.bars, ['abev3', '--period', 'daily', '--count', '1', '--view', 'var'])
        self.assertEqual(run.output, ' ASC -0.38\n')

    def test_exibe_o_atr_do_diario_da_abev3_de_14_periodos(self):
        run = self.runner.invoke(cli.atr, ['abev3', '--period', 'daily', '--count', '14'])
        self.assertEqual(run.output, '0.34\n')


if __name__ == '__main__':
    unittest.main()
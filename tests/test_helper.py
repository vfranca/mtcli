#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from click.testing import CliRunner
from cli_trade import _helper
from cli_trade.lib.bar import Bar
from cli_trade import cli


class TestHelper(unittest.TestCase):
    """Tests for `cli_trade` package."""

    def setUp(self):
        self.bar = Bar([
            '2015.04.01',
            '51187.00000',
            '56965.00000',
            '51187.00000',
            '56229.00000',
            '14628859',
            '8158109400'
        ])

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_calcula_o_ponto_medio_da_barra(self):
        self.assertEqual(_helper.get_medium_point(self.bar), 54076.00)

    def test_calcula_variacao_percentual_de_duas_barras(self):
        self.assertEqual(_helper.get_var(104300, 106250), 1.87)

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'cli_trade.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

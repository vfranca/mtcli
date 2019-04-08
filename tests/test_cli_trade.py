#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from click.testing import CliRunner
from cli_trade.cli_trade import *
from cli_trade import cli


class TestCli_trade(unittest.TestCase):
    """Tests for `cli_trade` package."""

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def _test_filtro_por_data(self):
        candles = reader(self.file, times = 2, date = "2018.09.13")
        self.assertEqual(candles[0], "107   branco33r15 neutral 76244 76199 76229 * 76222 76266")
        candles = reader(self.file, date = "2018.09.13")
        self.assertEqual(candles[0], "1  forte branco88r111 bottom0 77359 77233 77344 * 77296 77422")

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'cli_trade.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

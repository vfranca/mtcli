#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from click.testing import CliRunner
from cli_trade import cli_trade
from cli_trade import cli


class TestCli_trade(unittest.TestCase):
    """Tests for `cli_trade` package."""

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'cli_trade.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

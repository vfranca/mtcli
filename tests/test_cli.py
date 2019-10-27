#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from click.testing import CliRunner
from cli_trade import cli


class TestCli(unittest.TestCase):
    """Tests for `cli_trade` package."""

    def setUp(self):
        """Configura test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def _test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.atr, ['win$n'])
        assert result.exit_code == 0
        assert 'cli_trade.cli.atr' in result.output
        help_result = runner.invoke(cli.atr, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

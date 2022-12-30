from unittest import TestCase, mock, skip
from click.testing import CliRunner
from mtcli.rm import rm


class TestRM(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_exibe_o_range_medio_do_diario_da_abev3_de_14_periodos(self):
        res = self.runner.invoke(
            rm, ["abev3", "--period", "d1", "--count", "14"]
        )
        self.assertEqual(res.output, "0.34\n")
        self.assertEqual(res.exit_code, 0)

# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from mtcli.mt import mt


run = CliRunner()


def test_exibe_o_range_medio_do_diario_da_abev3_de_14_periodos():
    res = run.invoke(mt, ["rm", "abev3", "--period", "d1", "--count", "14"])
    assert res.output == "0.34\n"
    assert res.exit_code == 0

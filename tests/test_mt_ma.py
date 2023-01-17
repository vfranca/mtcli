# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from mtcli.mt import mt


run = CliRunner()


def test_exibe_a_media_movel_exponencial():
    res = run.invoke(
        mt, ["ma", "ibov", "--period", "d1", "--count", "20", "--method", "exponential"]
    )
    assert res.output == "moving average\n"
    assert res.exit_code == 0

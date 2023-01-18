# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from mtcli.mt import mt


run = CliRunner()


def test_exibe_a_media_movel():
    res = run.invoke(mt, ["ma", "ibov", "--period", "D1", "--count", "20"])
    assert res.output == "up 108525.0\n"
    assert res.exit_code == 0

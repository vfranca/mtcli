# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from mtcli.mt import mt


run = CliRunner()


def test_exibe_a_versao():
    res = run.invoke(mt, ["--version"])
    assert res.output == "mtcli 0.27.dev2\n"

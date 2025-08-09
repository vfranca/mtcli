from click.testing import CliRunner
from mtcli.mt import mt


run = CliRunner()


def test_exibe_a_versao():
    res = run.invoke(mt, ["--version"])
    assert res.output == "mtcli 1.12.0\n"

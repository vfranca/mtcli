from click.testing import CliRunner
from pytest import mark
from mtcli.mt import mt


run = CliRunner()


def test_exibe_a_media_movel():
    res = run.invoke(mt, ["ma", "bbdc4", "--period", "D1", "--count", "20"])
    assert res.output == "flat 12.36\n"
    assert res.exit_code == 0

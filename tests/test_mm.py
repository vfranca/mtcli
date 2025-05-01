from click.testing import CliRunner
from mtcli.mt import mt


run = CliRunner()


def test_exibe_a_media_movel_simples():
    res = run.invoke(mt, ["mm", "bbdc4", "--period", "d1", "--count", "20"])
    assert res.output == "11.98\n"
    assert res.exit_code == 0

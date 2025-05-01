from click.testing import CliRunner
from mtcli.mt import mt


run = CliRunner()


def test_exibe_o_volume_medio():
    res = run.invoke(mt, ["vm", "bbdc4", "--period", "d1", "--count", "10"])
    assert res.output == "28390.9\n"
    assert res.exit_code == 0

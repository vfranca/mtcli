from click.testing import CliRunner
from mtcli.mt import mt


run = CliRunner()


def test_exibe_o_volume_tick_medio():
    res = run.invoke(
        mt, ["vm", "bbdc4", "--period", "d1", "--count", "10", "--type", "tick"]
    )
    assert res.output == "28390.9\n"
    assert res.exit_code == 0


def test_exibe_o_volume_real_medio():
    res = run.invoke(
        mt, ["vm", "bbdc4", "--period", "d1", "--count", "10", "--type", "real"]
    )
    assert res.output == "35336300.0\n"
    assert res.exit_code == 0

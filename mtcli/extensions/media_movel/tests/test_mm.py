from click.testing import CliRunner
from mtcli.mt import mt


run = CliRunner()


def test_exibe_a_media_movel_simples():
    res = run.invoke(
        mt, ["mm", "BBDC4", "--period", "d1", "--window", "20", "--limit", "1"]
    )
    assert res.output == "11.98    2025.02.27 00:00:00\n"
    assert res.exit_code == 0

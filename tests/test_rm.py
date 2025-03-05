from click.testing import CliRunner
from pytest import mark
from mtcli.mt import mt


run = CliRunner()


def test_exibe_o_range_medio_do_diario():
    res = run.invoke(mt, ["rm", "ibov"])
    assert res.output == "1925.79\n"
    assert res.exit_code == 0

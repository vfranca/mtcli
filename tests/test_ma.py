from click.testing import CliRunner
from pytest import mark
from mtcli.mt import mt


run = CliRunner()


def test_exibe_a_ultima_media_movel():
    res = run.invoke(mt, ["ma", "bbdc4", "--period", "D1", "--count", "20"])
    assert res.output == "flat 12.36\n"
    assert res.exit_code == 0
    res = run.invoke(mt, ["ma", "spx500p", "--period", "m5", "--count", "20"])
    assert res.output == "flat 5148.00\n"


def test_exibe_a_media_movel_de_uma_data():
    res = run.invoke(
        mt, ["ma", "spx500p", "--period", "m5", "--count", "20", "--date", "2025-04-21"]
    )
    assert res.output == "down 5291.00\n"


def test_exibe_a_media_movel_de_uma_data_e_hora():
    res = run.invoke(
        mt,
        [
            "ma",
            "spx500p",
            "--period",
            "m5",
            "--count",
            "20",
            "--date",
            "2025-04-21",
            "--time",
            "09:20",
        ],
    )
    assert res.output == "flat 5245.00\n"

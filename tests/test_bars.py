import pytest
from click.testing import CliRunner
from mtcli.mt import mt


run = CliRunner()


def test_exibe_o_grafico_completo_doji():
    res = run.invoke(
        mt, ["bars", "abev3", "--view", "f", "--period", "d1", "--count", "1"]
    )
    assert res.output == "ASC  DOJI7R0.02  TOP64 18.57 18.29 18.37MP18.43 R0.28 -0.38\n"


def test_exibe_o_grafico_completo_de_rompimento_de_baixa():
    res = run.invoke(
        mt, ["bars", "bbdc4", "--view", "f", "--period", "d1", "--count", "1"]
    )
    assert (
        res.output
        == "DESC VD VERMELHO53R0.10 G0.03 TOP37 11.62 11.43 11.45MP11.52 R0.19 -0.78\n"
    )


def test_exibe_o_grafico_minimo():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "ch"]
    )
    assert res.output == "ASC 18.57 18.29\n"


def test_exibe_o_grafico_de_fechamentos():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "c"]
    )
    assert res.output == "18.37\n"


def test_exibe_o_grafico_de_maximas():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "h"]
    )
    assert res.output == "18.57\n"


def test_exibe_o_grafico_de_minimas():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "l"]
    )
    assert res.output == "18.29\n"


def test_exibe_o_grafico_de_volume():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "vol"]
    )
    assert res.output == "16466\n"


def test_exibe_o_grafico_de_ranges():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "r"]
    )
    assert res.output == "ASC VERMELHO 0.28\n"


def test_exibe_o_grafico_de_variacoes_percentuais():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "var"]
    )
    assert res.output == "-0.38%\n"

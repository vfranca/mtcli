import pytest
from click.testing import CliRunner
from mtcli.mt import mt


run = CliRunner()


def test_exibe_a_view_completo_doji():
    res = run.invoke(
        mt, ["bars", "abev3", "--view", "f", "--period", "d1", "--count", "1"]
    )
    assert res.output == "ASC  DOJI7  TOP64 18.57 18.29 18.37M18.43 R0.28\n"


def test_exibe_a_view_completo_de_rompimento_de_baixa():
    res = run.invoke(
        mt, ["bars", "bbdc4", "--view", "f", "--period", "d1", "--count", "1"]
    )
    assert res.output == "DESC V VERMELHO53 G0.03 TOP37 11.62 11.43 11.45M11.52 R0.19\n"


def test_exibe_a_view_minimo():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "ch"]
    )
    assert res.output == "ASC 18.57 18.29\n"


def test_exibe_a_view_de_fechamentos():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "c"]
    )
    assert res.output == "18.37\n"


def test_exibe_a_view_de_maximas():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "h"]
    )
    assert res.output == "18.57\n"


def test_exibe_a_view_de_minimas():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "l"]
    )
    assert res.output == "18.29\n"


def test_exibe_a_view_de_volume():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "vol"]
    )
    assert res.output == "16466\n"


def test_exibe_a_view_de_ranges():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "r"]
    )
    assert res.output == "ASC VERMELHO 0.28\n"


def test_exibe_a_view_de_variacoes_percentuais():
    res = run.invoke(
        mt, ["bars", "abev3", "--period", "d1", "--count", "1", "--view", "var"]
    )
    assert res.output == "-0.38%\n"


def test_exibe_view_minima_com_data():
    res = run.invoke(
        mt, ["bars", "bbdc4", "--view", "ch", "--show-date", "--count", "1"]
    )
    assert res.output == "2025.02.27 DESC 11.62 11.43\n"


def test_exibe_view_minima_com_data_e_numerador_ativados():
    res = run.invoke(
        mt,
        ["bars", "bbdc4", "--view", "ch", "--show-date", "--numerator", "--count", "1"],
    )
    assert res.output == "2025.02.27 DESC 11.62 11.43\n"
    res = run.invoke(
        mt,
        [
            "bars",
            "bbdc4",
            "--view",
            "ch",
            "--show-date",
            "--numerator",
            "--count",
            "1",
            "--period",
            "w1",
        ],
    )
    assert res.output == "2025.03.09 ASC 12.20 11.27\n"
    res = run.invoke(
        mt,
        [
            "bars",
            "bbdc4",
            "--view",
            "ch",
            "--show-date",
            "--numerator",
            "--count",
            "1",
            "--period",
            "mn1",
        ],
    )
    assert res.output == "2025.03.01 IB 12.20 11.22\n"


def test_exibe_view_completa_com_data_ativada():
    res = run.invoke(
        mt, ["bars", "bbdc4", "--view", "f", "--count", "1", "--show-date"]
    )
    assert (
        res.output
        == "2025.02.27 DESC V VERMELHO53 G0.03 TOP37 11.62 11.43 11.45M11.52 R0.19\n"
    )


def test_exibe_view_ranges_com_data_ativada():
    res = run.invoke(
        mt, ["bars", "bbdc4", "--view", "r", "--count", "1", "--show-date"]
    )
    assert res.output == "2025.02.27 DESC VERMELHO 0.19\n"


def test_exibe_view_da_variacao_percentual_com_data():
    res = run.invoke(
        mt, ["bars", "bbdc4", "--view", "var", "--count", "1", "--show-date"]
    )
    assert res.output == "2025.02.27 -0.78%\n"


def test_exibe_view_volume_com_data():
    res = run.invoke(
        mt, ["bars", "bbdc4", "--view", "vol", "--count", "1", "--show-date"]
    )
    assert res.output == "2025.02.27 19949\n"


def test_exibe_view_aberturas_com_data():
    res = run.invoke(
        mt, ["bars", "bbdc4", "--view", "o", "--count", "1", "--show-date"]
    )
    assert res.output == "2025.02.27 11.55\n"


def test_exibe_view_maximas_com_data():
    res = run.invoke(
        mt, ["bars", "bbdc4", "--view", "h", "--count", "1", "--show-date"]
    )
    assert res.output == "2025.02.27 11.62\n"


def test_exibe_view_minimas_com_data():
    res = run.invoke(
        mt, ["bars", "bbdc4", "--view", "l", "--count", "1", "--show-date"]
    )
    assert res.output == "2025.02.27 11.43\n"


def test_exibe_view_fechamentos_com_data():
    res = run.invoke(
        mt, ["bars", "bbdc4", "--view", "c", "--count", "1", "--show-date"]
    )
    assert res.output == "2025.02.27 11.45\n"


def test_exibe_intraday_com_numerador_desativado():
    res = run.invoke(
        mt,
        [
            "bars",
            "wdov24",
            "--period",
            "m5",
            "--date",
            "2024.09.27",
            "--count",
            "1",
            "--view",
            "ch",
        ],
    )
    assert res.output == "OB 5436.00 5428.00\n"


def test_exibe_intraday_com_numerador_ativado():
    res = run.invoke(
        mt,
        [
            "bars",
            "wdov24",
            "--period",
            "m5",
            "--date",
            "2024.09.27",
            "--count",
            "1",
            "--view",
            "ch",
            "--numerator",
        ],
    )
    assert res.output == "103 OB 5436.00 5428.00\n"


def test_exibe_view_no_m1():
    res = run.invoke(
        mt, ["bars", "wdoj25", "--view", "f", "--period", "m1", "--count", "1"]
    )
    assert (
        res.output == " V VERMELHO50  BOTTOM50 5770.00 5769.00 5769.50M5769.50 R1.00\n"
    )


def test_exibe_view_no_m2():
    res = run.invoke(
        mt, ["bars", "wdoj25", "--view", "f", "--period", "m2", "--count", "1"]
    )
    assert res.output == "IB C VERDE50  TOP50 5770.00 5769.00 5769.50M5769.50 R1.00\n"


def test_exibe_view_no_m3():
    res = run.invoke(
        mt, ["bars", "wdoj25", "--view", "f", "--period", "m3", "--count", "1"]
    )
    assert (
        res.output
        == "IB V VERMELHO80  BOTTOM20 5771.50 5769.00 5769.50M5770.25 R2.50\n"
    )


def test_exibe_view_no_m4():
    res = run.invoke(
        mt, ["bars", "wdoj25", "--view", "f", "--period", "m2", "--count", "1"]
    )
    assert res.output == "IB C VERDE50  TOP50 5770.00 5769.00 5769.50M5769.50 R1.00\n"


def test_exibe_view_no_m5():
    res = run.invoke(
        mt, ["bars", "wdoj25", "--view", "f", "--period", "m5", "--count", "1"]
    )
    assert res.output == "  VERDE17  TOP83 5772.00 5769.00 5769.50M5770.50 R3.00\n"

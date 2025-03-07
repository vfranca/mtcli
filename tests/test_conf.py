from click.testing import CliRunner
from pytest import mark
from mtcli.mt import mt


run = CliRunner()


def test_exibe_uma_lista_de_variaveis_de_ambiente_disponiveis():
    res = run.invoke(mt, ["conf"])
    assert (
        res.output
        == "DIGITOS=0\nLATERAL=DOJI\nALTA=VERDE\nBAIXA=VERMELHO\nROMPIMENTO_ALTA=CP\nROMPIMENTO_BAIXA=VD\nPERCENTUAL_DOJI=10\nPERCENTUAL_ROMPIMENTO=50\nMT5_PASTA=C:/Users/Administrador/cli/mtcli/tests/fixtures/Files\n"
    )


def test_altera_a_quantidade_de_digitos_da_moeda():
    res = run.invoke(mt, ["conf", "--digitos", "0"])
    assert res.output == "DIGITOS=0\n"


def test_altera_o_nome_da_barra_lateral():
    res = run.invoke(mt, ["conf", "--lateral", "doji"])
    assert res.output == "LATERAL=DOJI\n"


def test_altera_o_nome_da_barra_de_alta():
    res = run.invoke(mt, ["conf", "--alta", "verde"])
    assert res.output == "ALTA=VERDE\n"


def test_altera_o_nome_da_barra_de_baixa():
    res = run.invoke(mt, ["conf", "--baixa", "vermelho"])
    assert res.output == "BAIXA=VERMELHO\n"


def test_altera_a_abreviatura_da_barra_de_rompimento_de_alta():
    res = run.invoke(mt, ["conf", "--rompimento-alta", "cp"])
    assert res.output == "ROMPIMENTO_ALTA=CP\n"


def test_altera_a_abreviatura_da_barra_de_rompimento_de_baixa():
    res = run.invoke(mt, ["conf", "--rompimento-baixa", "vd"])
    assert res.output == "ROMPIMENTO_BAIXA=VD\n"


def test_altera_o_percentual_do_corpo_da_barra_doji():
    res = run.invoke(mt, ["conf", "--percentual-doji", "10"])
    assert res.output == "PERCENTUAL_DOJI=10\n"


def test_altera_o_percentual_do_corpo_da_barra_de_rompimento():
    res = run.invoke(mt, ["conf", "--percentual-rompimento", "50"])
    assert res.output == "PERCENTUAL_ROMPIMENTO=50\n"


def test_altera_o_caminho_da_pasta_do_mt5():
    res = run.invoke(
        mt,
        [
            "conf",
            "--mt5-pasta",
            "C:/Users/Administrador/cli/mtcli/tests/fixtures/Files",
        ],
    )
    assert (
        res.output
        == "MT5_PASTA=C:/Users/Administrador/cli/mtcli/tests/fixtures/Files\n"
    )

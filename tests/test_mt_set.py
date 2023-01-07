# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from mtcli.mt import mt


run = CliRunner()


def test_exibe_uma_lista_de_variaveis_de_ambiente_disponiveis():
    res = run.invoke(mt, ["set"])
    assert (
        res.output
        == "DIGITS=2\nLATERAL=DOJI\nALTA=VERDE\nBAIXA=VERMELHO\nPRESSAO_COMPRA=CP\nPRESSAO_VENDA=VD\nPERCENTUAL_LATERAL=10\nPERCENTUAL_ROMPIMENTO=50\nCSV_PATH=C:/Users/Administrador/git/mtcli/tests/fixtures/Files\n"
    )

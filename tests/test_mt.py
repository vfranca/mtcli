from click.testing import CliRunner
from mtcli.mt import mt


run = CliRunner()


def test_exibe_a_versao():
    res = run.invoke(mt, ["--version"])
    assert res.output == "mtcli 1.10.0\n"


def test_exibe_msg_de_excecao_quando_um_arquivo_csv_nao_e_encontrado():
    res = run.invoke(mt, ["bars", "XXXX"])
    assert res.output == "XXXXd1 nao encontrado! Tente novamente\n"

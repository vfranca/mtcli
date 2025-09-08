import pytest
import configparser
from pathlib import Path

from mtcli import conf


def test_config_sem_cabecalho(tmp_path, monkeypatch):
    # Cria um arquivo mtcli.ini inválido (sem seção)
    ini_invalido = tmp_path / "mtcli.ini"
    ini_invalido.write_text("DIGITOS='0'\n")

    # Substitui CONFIG_PATH pelo caminho temporário
    monkeypatch.setattr(conf, "CONFIG_PATH", str(ini_invalido))

    with pytest.raises(SystemExit) as excinfo:
        conf.carregar_config()

    assert excinfo.type == SystemExit
    assert excinfo.value.code == 1

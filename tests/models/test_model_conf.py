"""
testes:
    1. Carregamento de config válido
2. Erro ao carregar config malformado
3. Salvamento de config
"""

import os
import tempfile
import pytest
from mtcli.models.model_conf import ConfModel, ConfigFormatError
import configparser


def test_carregar_config_valido():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write("[padrao]\nCHAVE=valor\n")
        f.flush()
        model = ConfModel(f.name)
        config = model.carregar()
        assert config.get("padrao", "CHAVE") == "valor"
    os.remove(f.name)


def test_carregar_config_invalido():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write("CHAVE=valor\n")  # Sem seção
        f.flush()
        model = ConfModel(f.name)
        with pytest.raises(ConfigFormatError):
            model.carregar()
    os.remove(f.name)


def test_salvar_config():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        path = f.name
    model = ConfModel(path)
    config = configparser.ConfigParser()
    config["padrao"] = {"CHAVE": "valor"}
    model.salvar(config)

    # Verifica se o conteúdo foi salvo corretamente
    novo_model = ConfModel(path)
    carregado = novo_model.carregar()
    assert carregado.get("padrao", "CHAVE") == "valor"
    os.remove(path)

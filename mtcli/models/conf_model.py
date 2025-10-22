"""Modelo de configurações."""

import configparser
from configparser import MissingSectionHeaderError
import os


class ConfigFormatError(Exception):
    pass


class ConfModel:
    def __init__(self, configuracoes):
        self.CONFIG_PATH = os.path.abspath(configuracoes)

    def carregar(self):
        config = configparser.ConfigParser()
        if os.path.exists(self.CONFIG_PATH):
            try:
                config.read(self.CONFIG_PATH)
            except MissingSectionHeaderError:
                raise ConfigFormatError(
                    f"Erro: o arquivo '{self.CONFIG_PATH}' não contém seções válidas.\n"
                    "Certifique-se de que ele está no formato correto:\n[padrao]\nCHAVE=valor"
                )
        else:
            config["DEFAULT"] = {}
        return config

    def salvar(self, config):
        with open(self.CONFIG_PATH, "w") as f:
            config.write(f)

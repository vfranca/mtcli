"""
Registry de configurações do mtcli.

Plugins podem registrar suas opções de configuração aqui
para permitir descoberta automática via CLI.
"""


class ConfigOption:
    """
    Representa uma opção de configuração registrada.
    """

    def __init__(self, section, name, type=str, default=None, description=""):
        self.section = section
        self.name = name
        self.type = type
        self.default = default
        self.description = description


class ConfigRegistry:
    """
    Registro central de opções de configuração.
    """

    def __init__(self):
        self._options = []

    def register(self, section, name, type=str, default=None, description=""):
        option = ConfigOption(section, name, type, default, description)
        self._options.append(option)

    def get_all(self):
        return self._options

    def get_section(self, section):
        return [o for o in self._options if o.section == section]


registry = ConfigRegistry()

"""
Gerenciador central de plugins do mtcli.
"""


class PluginManager:
    """
    Registry central de plugins e extensões.
    """

    def __init__(self):

        self.commands = []
        self.data_sources = {}
        self.chart_types = {}

    def register_command(self, command):
        self.commands.append(command)

    def register_data_source(self, name, cls):
        self.data_sources[name] = cls

    def register_chart(self, name, cls):
        self.chart_types[name] = cls


plugin_manager = PluginManager()

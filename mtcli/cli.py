"""
CLI principal do mtcli.

Este módulo define o grupo principal `mt`
e inicializa o carregamento de plugins.
"""

import click

from mtcli.plugin_loader import load_plugins
from .commands.bars import bars


@click.group(context_settings={"max_content_width": 120})
@click.version_option(package_name="mtcli")
def mt():
    """
    CLI principal do mtcli.

    Exibe gráficos e informações de mercado
    em formato textual compatível com leitores de tela.
    """
    pass


mt.add_command(bars, name="bars")


# Carrega plugins automaticamente
load_plugins(mt)


if __name__ == "__main__":
    mt()

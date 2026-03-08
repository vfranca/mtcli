"""
CLI principal do mtcli.

Este módulo define o grupo principal `mt`
e inicializa o carregamento de plugins.
"""

import click

from mtcli.plugin_loader import load_plugins
from mtcli.logger import setup_logger

from .commands.bars import bars
from .commands.doctor import doctor
from .commands.migrate import migrate


logger = setup_logger(__name__)


@click.group(context_settings={"max_content_width": 120})
@click.version_option(package_name="mtcli")
def mt():
    """
    CLI principal do mtcli.

    Exibe gráficos e informações de mercado
    em formato textual compatível com leitores de tela.
    """
    pass


# ---------------------------------------------------------
# Comandos internos
# ---------------------------------------------------------

mt.add_command(doctor, name="doctor")
mt.add_command(bars, name="bars")
mt.add_command(doctor, name="dr")
mt.add_command(migrate)


# ---------------------------------------------------------
# Carregamento de plugins
# ---------------------------------------------------------

loaded_plugins = load_plugins(mt)

logger.info("Plugins carregados: %s", loaded_plugins)


# ---------------------------------------------------------
# Comando utilitário: listar plugins
# ---------------------------------------------------------

@mt.command(name="plugins")
def list_plugins():
    """
    Lista os plugins atualmente carregados no mtcli.
    """

    if not loaded_plugins:
        click.echo("Nenhum plugin carregado.")
        return

    click.echo("Plugins carregados:\n")

    for name in loaded_plugins:
        click.echo(f"  {name}")


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------

if __name__ == "__main__":
    mt()

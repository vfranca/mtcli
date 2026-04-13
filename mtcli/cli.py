"""
CLI principal do mtcli.
"""

import os
import click
from .plugin_loader import load_plugins
from .logger import setup_logger

from .commands.bars import bars
from .commands.doctor import doctor

logger = setup_logger(__name__)


@click.group(context_settings={"max_content_width": 120}, invoke_without_command=True)
@click.version_option(package_name="mtcli")
@click.pass_context
def mt(ctx):
    """
    CLI principal do mtcli.
    """

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


mt.add_command(doctor, name="doctor")
mt.add_command(bars, name="bars")

loaded_plugins = load_plugins(mt)
logger.info("Plugins carregados: %s", loaded_plugins)


@mt.command(name="plugins")
def list_plugins():
    """
    Lista os plugins carregados no mtcli.
    """

    if not loaded_plugins:
        click.echo("Nenhum plugin carregado.")
        return

    click.echo("Plugins carregados:\n")
    for name in loaded_plugins:
        click.echo(f"  {name}")


if __name__ == "__main__":
    mt()

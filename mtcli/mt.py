"""Módulo principal do aplicativo."""

import click

from mtcli import __version__
from mtcli.bars import bars
from mtcli.conf import conf


try:
    from importlib.metadata import entry_points
except ImportError:
    from importlib_metadata import entry_points  # Para Python < 3.8


@click.group(invoke_without_command=True)
@click.option("--version", "-v", is_flag=True, help="Exibe a versao do mtcli.")
def mt(version):
    """Exibe o grafico do MetaTrader 5 em texto."""
    if version:
        click.echo("mtcli %s" % __version__)
        return


mt.add_command(bars, name="bars")
mt.add_command(conf, name="conf")


def load_plugins():
    eps = entry_points()
    plugins = (
        eps.select(group="mtcli.plugins")
        if hasattr(eps, "select")
        else eps.get("mtcli.plugins", [])
    )
    for ep in plugins:
        cmd = ep.load()
        mt.add_command(cmd)


load_plugins()


if __name__ == "__main__":
    mt()

"""Módulo principal do aplicativo."""

import click

from mtcli.bars import bars
from mtcli.conf import conf
from mtcli.logs import logs


try:
    from importlib.metadata import entry_points
except ImportError:
    from importlib_metadata import entry_points  # Para Python < 3.8


@click.group()
@click.version_option(package_name="mtcli")
def mt():
    """Exibe o grafico do MetaTrader 5 em texto."""
    pass


mt.add_command(bars, name="bars")
mt.add_command(conf, name="conf")
mt.add_command(logs, name="logs")


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

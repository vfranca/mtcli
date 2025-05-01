"""
Módulo principal do aplicativo.

Frontcontroller do mtcli.
"""

import click

from mtcli import __version__
from mtcli.bars import bars
from mtcli.conf import conf
from mtcli.ma import ma
from mtcli.mm import mm
from mtcli.rm import rm
from mtcli.vm import vm


@click.group(invoke_without_command=True)
@click.option("--version", "-v", is_flag=True, help="Exibe a versao do mtcli.")
def mt(version):
    """Exibe o grafico de velas do MetaTrader 5 em texto."""
    if version:
        click.echo("mtcli %s" % __version__)
        return 0


mt.add_command(bars)
mt.add_command(mm)
mt.add_command(rm)
mt.add_command(conf)
mt.add_command(ma)
mt.add_command(vm)


if __name__ == "__main__":
    mt()

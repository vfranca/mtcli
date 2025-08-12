"""
Módulo principal do aplicativo.

Frontcontroller do mtcli.
"""

import click

from mtcli import __version__
from mtcli.bars import bars
from mtcli.conf import conf
from mtcli.extensions import (
    agressao,
    media_movel,
    moving_average,
    range_medio,
    volume_medio,
)


@click.group(invoke_without_command=True)
@click.option("--version", "-v", is_flag=True, help="Exibe a versao do mtcli.")
def mt(version):
    """Exibe o grafico de velas do MetaTrader 5 em texto."""
    if version:
        click.echo("mtcli %s" % __version__)
        return


mt.add_command(bars)
mt.add_command(conf)
mt.add_command(media_movel.mm)
mt.add_command(range_medio.rm)
mt.add_command(moving_average.ma)
mt.add_command(volume_medio.vm)
mt.add_command(agressao.sa)


if __name__ == "__main__":
    mt()

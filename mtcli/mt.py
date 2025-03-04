"""
Aplicativo CLI para exibir gráficos do MetaTrader 5
"""
import click
from mtcli import conf
from mtcli import __version__
from mtcli.bars import bars
from mtcli.mm import mm
from mtcli.rm import rm
from mtcli.set import set
from mtcli.ma import ma


@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, help="Exibe a versao")
def mt(version):
    """Exibe graficos do MetaTrader 5."""
    if version:
        click.echo("mtcli %s" % __version__)
        return 0


mt.add_command(bars)
mt.add_command(mm)
mt.add_command(rm)
mt.add_command(set)
mt.add_command(ma)


if __name__ == "__main__":
    mt()

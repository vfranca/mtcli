"""
CLI principal do mtcli.

Responsável por:

- inicializar o ambiente do CLI
- carregar plugins
- iniciar captura automática de ticks (opcional)

A captura automática é ativada se a variável de ambiente
MTCLI_SYMBOL estiver definida.

Exemplo:

    MTCLI_SYMBOL=WIN$N mt bars

Nesse caso o mtcli inicia um TickEngine em background
para manter o histórico de ticks atualizado.
"""

import os
import click

from mtcli.plugin_loader import load_plugins
from mtcli.logger import setup_logger
from mtcli.marketdata.tick_engine import TickEngine

from .commands.bars import bars
from .commands.doctor import doctor
from .commands.migrate import migrate
from .commands.ticks import ticks


logger = setup_logger(__name__)

_tick_engine = None


def start_tick_capture():
    """
    Inicia captura contínua de ticks em background.

    Se a variável de ambiente MTCLI_SYMBOL estiver definida,
    o mtcli iniciará automaticamente um TickEngine para
    coletar ticks continuamente.

    Isso permite manter um histórico próprio de ticks
    independente do histórico do broker.
    """

    global _tick_engine

    if _tick_engine:
        return

    symbol = os.getenv("MTCLI_SYMBOL")

    if not symbol:
        logger.info("Captura automática de ticks desativada (MTCLI_SYMBOL não definido).")
        return

    logger.info("Iniciando captura contínua de ticks para %s", symbol)

    try:

        _tick_engine = TickEngine([symbol])
        _tick_engine.start()

        logger.info("Captura de ticks iniciada em background.")

    except Exception:
        logger.exception("Falha ao iniciar captura de ticks")


@click.group(context_settings={"max_content_width": 120}, invoke_without_command=True)
@click.version_option(package_name="mtcli")
@click.pass_context
def mt(ctx):
    """
    CLI principal do mtcli.
    """

    start_tick_capture()

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


mt.add_command(doctor, name="doctor")
mt.add_command(bars, name="bars")
mt.add_command(doctor, name="dr")
mt.add_command(migrate)
mt.add_command(ticks)

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

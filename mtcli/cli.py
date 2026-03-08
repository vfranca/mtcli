"""
CLI principal do mtcli.
"""

import os
import threading
import click

from mtcli.plugin_loader import load_plugins
from mtcli.logger import setup_logger
from mtcli.marketdata.tick_streamer import TickStreamer

from .commands.bars import bars
from .commands.doctor import doctor
from .commands.migrate import migrate


logger = setup_logger(__name__)

_tick_streamer = None


def start_tick_capture():
    """
    Inicia captura contínua de ticks em background.

    O símbolo deve ser definido via variável:

        MTCLI_SYMBOL=WINJ26
    """

    global _tick_streamer

    if _tick_streamer:
        return

    symbol = os.getenv("MTCLI_SYMBOL")

    if not symbol:
        logger.info("Captura de ticks desativada (MTCLI_SYMBOL não definido).")
        return

    logger.info("Iniciando captura contínua de ticks para %s", symbol)

    try:

        _tick_streamer = TickStreamer(symbol)

        thread = threading.Thread(
            target=_tick_streamer.start,
            daemon=True,
            name="mtcli-tick-streamer",
        )

        thread.start()

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

loaded_plugins = load_plugins(mt)

logger.info("Plugins carregados: %s", loaded_plugins)


@mt.command(name="plugins")
def list_plugins():
    """
    Lista os plugins carregados.
    """

    if not loaded_plugins:
        click.echo("Nenhum plugin carregado.")
        return

    click.echo("Plugins carregados:\n")

    for name in loaded_plugins:
        click.echo(f"  {name}")


if __name__ == "__main__":
    mt()

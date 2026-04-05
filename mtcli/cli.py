"""
CLI principal do mtcli.
"""

import os
import click
from mtcli.plugin_loader import load_plugins
from mtcli.logger import setup_logger
from mtcli.services.tick_service import ensure_tick_engine

from .commands.bars import bars
from .commands.doctor import doctor
from .commands.ticks import ticks
from .commands.backfill import backfill

logger = setup_logger(__name__)

_tick_engines = []


def start_tick_capture():
    """
    Inicia captura contínua de ticks em background se MTCLI_SYMBOL estiver definido.
    """

    global _tick_engines

    if _tick_engines:
        return

    symbols = os.getenv("MTCLI_SYMBOL")

    if not symbols:
        logger.info(
            "Captura automática de ticks desativada (MTCLI_SYMBOL não definido)."
        )
        return

    if isinstance(symbols, str):
        symbols = [symbols]

    logger.info("Iniciando captura contínua de ticks para %s", symbols)

    try:
        for symbol in symbols:
            engine = ensure_tick_engine(symbol)
            _tick_engines.append(engine)
            # pode rodar em thread se quiser background
            import threading
            t = threading.Thread(target=engine.start, daemon=True)
            t.start()

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
mt.add_command(ticks)
mt.add_command(backfill, name="fill")

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

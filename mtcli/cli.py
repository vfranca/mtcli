"""
CLI principal do mtcli.

Este módulo define o grupo principal `mt`
e inicializa o carregamento de plugins.

Também inicia a captura contínua de ticks para manter
um histórico próprio independente do broker.
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


# ---------------------------------------------------------
# Configuração de captura de ticks
# ---------------------------------------------------------

_tick_streamer = None


def start_tick_capture():
    """
    Inicia captura contínua de ticks em background.

    O símbolo pode ser configurado via variável de ambiente:

        MTCLI_SYMBOL=WINJ26
    """

    global _tick_streamer

    if _tick_streamer:
        return

    symbol = os.getenv("SYMBOL")

    if not symbol:
        logger.info("Captura de ticks desativada (MTCLI_SYMBOL não definido).")
        return

    logger.info("Iniciando captura contínua de ticks para %s", symbol)

    _tick_streamer = TickStreamer(symbol)

    thread = threading.Thread(
        target=_tick_streamer.start,
        daemon=True,
        name="mtcli-tick-streamer",
    )

    thread.start()

    logger.info("Captura de ticks iniciada em background.")


# ---------------------------------------------------------
# CLI principal
# ---------------------------------------------------------

@click.group(context_settings={"max_content_width": 120}, invoke_without_command=True)
@click.version_option(package_name="mtcli")
@click.pass_context
def mt(ctx):
    """
    CLI principal do mtcli.

    Exibe gráficos e informações de mercado
    em formato textual compatível com leitores de tela.
    """

    # inicia captura de ticks
    start_tick_capture()

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


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

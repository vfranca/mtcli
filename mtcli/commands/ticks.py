"""
Comando CLI para captura contínua de ticks.

Exemplo:
    mt ticks WIN$N
    mt ticks WIN$N WDO$N PETR4
"""

import click
import threading

from mtcli.services.tick_service import ensure_tick_engine
from mtcli.logger import setup_logger

logger = setup_logger(__name__)


@click.command()
@click.argument("symbols", nargs=-1)
def ticks(symbols):

    if not symbols:

        click.echo("Informe ao menos um símbolo.")
        return

    engines = []

    for symbol in symbols:

        engine = ensure_tick_engine(symbol)

        t = threading.Thread(
            target=engine.start,
            daemon=True
        )

        t.start()

        engines.append(engine)

        click.echo(
            f"Captura de ticks iniciada para {symbol}"
        )

    try:

        while True:

            for engine in engines:
                pass

    except KeyboardInterrupt:

        click.echo("\nEncerrando captura...")

        for engine in engines:
            engine.stop()

"""
Comando CLI para captura contínua de ticks.

Permite iniciar o serviço de captura de ticks
para um ou mais símbolos.

Exemplo:

    mt ticks WIN$N
    mt ticks WIN$N WDO$N PETR4
"""

import time
import click

from mtcli.services.tick_service import ensure_tick_engine


@click.command()
@click.argument("symbols", nargs=-1)
def ticks(symbols):

    if not symbols:
        click.echo("Informe ao menos um símbolo.")
        return

    engine = ensure_tick_engine(symbols)

    click.echo("Captura de ticks iniciada.")

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        click.echo("\nEncerrando captura de ticks...")
        engine.stop()

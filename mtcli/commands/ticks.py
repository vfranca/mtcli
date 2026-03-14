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
    """
    Inicia captura contínua de ticks.
    """

    if not symbols:
        click.echo("Informe ao menos um símbolo.")
        return

    # atualmente o engine suporta apenas 1 símbolo
    symbol = symbols[0]

    engine = ensure_tick_engine(symbol)

    click.echo(f"Captura de ticks iniciada para {symbol}")

    try:
        # inicia engine
        engine.start()

    except KeyboardInterrupt:

        click.echo("\nEncerrando captura de ticks...")
        engine.stop()

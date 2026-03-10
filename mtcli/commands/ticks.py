"""
Comando CLI para captura contínua de ticks.

Permite iniciar um TickEngine manualmente
para um ou mais símbolos.

Exemplo:

    mt ticks WIN$N
    mt ticks WIN$N WDO$N PETR4

A captura continua até o usuário interromper
com Ctrl+C.
"""

import time
import click

from mtcli.marketdata.tick_engine import TickEngine


@click.command()
@click.argument("symbols", nargs=-1)
def ticks(symbols):
    """
    Inicia captura contínua de ticks para os símbolos informados.
    """

    if not symbols:
        click.echo("Informe ao menos um símbolo.")
        return

    engine = TickEngine(symbols)

    click.echo("Iniciando captura de ticks...")

    engine.start()

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        click.echo("\nEncerrando captura de ticks...")
        engine.stop()

"""
CLI: ticks

Inicializa a captura contínua de ticks em tempo real para um ou
mais símbolos, utilizando uma arquitetura event-driven baseada
em filas e processamento assíncrono.

Arquitetura:

TickEngine (polling MT5)
    -> Raw TickBus (queue)
    -> TradeTickFilter
    -> Trade TickBus (queue)
    -> TickWriter (batch + async)
    -> TickRepository
    -> SQLite

Características:

- Suporte multi-símbolo
- Threads independentes por símbolo
- Pipeline desacoplado (não bloqueante)
- Encerramento gracioso (CTRL+C)

Uso:
    mt ticks WIN$N
    mt ticks WIN$N WDO$N PETR4
"""

import time
import threading
import click

from ..services.tick_service import ensure_tick_engine
from ..logger import setup_logger

logger = setup_logger(__name__)


@click.command()
@click.argument("symbols", nargs=-1)
def ticks(symbols):
    """
    Inicia captura contínua de ticks.

    Parameters
    ----------
    symbols : tuple[str]
        Lista de símbolos a monitorar.

    Notas
    -----
    - Cada símbolo possui um TickEngine dedicado.
    - O pipeline downstream é totalmente assíncrono.
    """

    if not symbols:
        click.echo("Informe ao menos um símbolo.")
        return

    engines = []
    threads = []

    for symbol in symbols:

        engine = ensure_tick_engine(symbol)

        thread = threading.Thread(
            target=engine.start,
            name=f"TickEngine-{symbol}",
            daemon=True,
        )

        thread.start()

        engines.append(engine)
        threads.append(thread)

        click.echo(f"Captura iniciada: {symbol}")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        click.echo("\nEncerrando...")

        for engine in engines:
            engine.stop()

        for engine in engines:
            engine.writer.stop()

        for engine in engines:
            engine.writer.join()

        for t in threads:
            t.join(timeout=2)

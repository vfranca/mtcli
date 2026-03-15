"""
Comando CLI: backfill

Responsável por carregar histórico de ticks do MetaTrader5
para o banco SQLite do mtcli utilizando o BackfillEngine.

Fluxo:

BackfillEngine
      ↓
TickBus
      ↓
TickWriter
      ↓
TickRepository
      ↓
SQLite
"""

import click

from mtcli.marketdata.backfill import BackfillEngine
from mtcli.marketdata.tick_bus import TickBus
from mtcli.marketdata.tick_repository import TickRepository
from mtcli.marketdata.tick_writer import TickWriter


@click.command()
@click.argument("symbol")
@click.option(
    "--days",
    default=5,
    show_default=True,
    help="Número de dias de histórico a carregar caso não exista histórico local.",
)
def backfill(symbol: str, days: int):
    """
    Executa backfill histórico de ticks.

    Este comando baixa ticks históricos diretamente do MetaTrader5
    e os grava no banco local SQLite do mtcli.

    O processo é incremental:

    - se já existirem ticks no banco, o backfill continua do último tick
    - caso contrário, carrega o número de dias definido em --days

    Examples
    --------

    Carregar 5 dias:

        mt fill WINJ26

    Carregar 30 dias:

        mt fill WINJ26 --days 30
    """

    bus = TickBus()

    repo = TickRepository()

    writer = TickWriter(symbol, repo)

    bus.subscribe(writer)

    engine = BackfillEngine(symbol, bus, repo)

    engine.run(days)

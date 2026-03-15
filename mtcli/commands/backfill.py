"""
Comando CLI: backfill

Responsável por carregar histórico de ticks do MetaTrader5
para o banco SQLite do mtcli utilizando o BackfillEngine.

Fluxo:

BackfillEngine
      ↓
TickRepository
      ↓
SQLite

Opcionalmente os ticks também podem ser publicados no TickBus
para que plugins consumam o fluxo histórico.
"""

import click

from mtcli.marketdata.backfill_engine import BackfillEngine
from mtcli.marketdata.tick_bus import TickBus
from mtcli.marketdata.tick_repository import TickRepository


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

    # Event bus (permite que plugins consumam os ticks históricos)
    bus = TickBus()

    # Repositório de persistência
    repo = TickRepository()

    # Engine de backfill
    engine = BackfillEngine(symbol, bus, repo)

    # Executa o carregamento histórico
    engine.run(days)

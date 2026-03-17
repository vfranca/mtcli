"""
Comando CLI: backfill

Carrega histórico de ticks do MetaTrader5
para o banco SQLite do mtcli utilizando o BackfillEngine
com filtro de trade ticks.

Fluxo:

BackfillEngine
      ->
raw_tick_bus
      ->
TradeTickFilter
      ->
trade_tick_bus
      ->
TickWriter / plugins
      ->
TickRepository
      ->
SQLite
"""

import click

from mtcli.logger import setup_logger
from mtcli.marketdata.tick_bus import TickBus
from mtcli.marketdata.tick_repository import TickRepository
from mtcli.marketdata.tick_writer import TickWriter
from mtcli.marketdata.trade_tick_filter import TradeTickFilter
from mtcli.marketdata.backfill_engine import BackfillEngine

logger = setup_logger(__name__)


@click.command()
@click.argument("symbol")
@click.option(
    "--days",
    default=5,
    show_default=True,
)
def backfill(symbol: str, days: int):

    raw_tick_bus = TickBus()
    trade_tick_bus = TickBus()

    repo = TickRepository()

    raw_tick_bus.subscribe(
        TradeTickFilter(trade_tick_bus)
    )

    writer = TickWriter(symbol, repo)

    trade_tick_bus.subscribe(writer)

    engine = BackfillEngine(
        symbol,
        raw_tick_bus,
        repo,
    )

    engine.run(days)

    logger.info(
        "Backfill concluído (%s) — trade ticks gravados",
        symbol,
    )

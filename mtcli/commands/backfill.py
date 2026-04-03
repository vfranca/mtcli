"""
Comando CLI: backfill

Responsável por carregar ticks históricos do MetaTrader5
para o banco SQLite utilizando um pipeline event-driven.

Fluxo:

BackfillEngine
    -> Raw TickBus (assíncrono)
    -> TradeTickFilter
    -> Trade TickBus (assíncrono)
    -> TickWriter (batch + fila + thread)
    -> TickRepository
    -> SQLite

IMPORTANTE:

Diferente do modelo síncrono, este pipeline é assíncrono.
Por isso, ao final do backfill é necessário aguardar o
esvaziamento das filas e flush final do writer para garantir
consistência dos dados.

Uso:
    mt backfill WIN$N --days 5
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
@click.option("--days", default=5, show_default=True)
def backfill(symbol: str, days: int):
    """
    Executa backfill de ticks para um símbolo.

    Parameters
    ----------
    symbol : str
        Ativo a ser carregado (ex: WIN$N)
    days : int
        Quantidade de dias retroativos
    """

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

    # 🔥 CRÍTICO: garantir consistência
    logger.info("Aguardando flush final do pipeline...")

    writer.flush()
    writer.stop()
    writer.join()

    logger.info(
        "Backfill concluído (%s) — dados persistidos com sucesso",
        symbol,
    )

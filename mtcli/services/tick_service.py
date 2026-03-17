"""
Tick Service

Inicializa pipeline completo de ticks.
"""

from mtcli.logger import setup_logger
from mtcli.marketdata.tick_engine import TickEngine
from mtcli.marketdata.tick_bus import TickBus
from mtcli.marketdata.tick_writer import TickWriter
from mtcli.marketdata.tick_repository import TickRepository
from mtcli.marketdata.trade_tick_filter import TradeTickFilter

logger = setup_logger(__name__)

_engine_instances = {}


def ensure_tick_engine(symbol: str) -> TickEngine:

    global _engine_instances

    if symbol in _engine_instances:

        logger.debug("TickEngine para %s já inicializado", symbol)

        return _engine_instances[symbol]

    logger.info("Inicializando TickEngine para %s", symbol)

    repository = TickRepository()

    raw_tick_bus = TickBus()
    trade_tick_bus = TickBus()

    raw_tick_bus.subscribe(
        TradeTickFilter(trade_tick_bus)
    )

    writer = TickWriter(symbol, repository)

    trade_tick_bus.subscribe(writer)

    engine = TickEngine(
        symbol=symbol,
        tick_bus=raw_tick_bus,
    )

    _engine_instances[symbol] = engine

    logger.info(
        "TickEngine inicializado com TradeTickFilter para %s",
        symbol,
    )

    return engine

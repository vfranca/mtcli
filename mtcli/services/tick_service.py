"""
Tick Service

Responsável por montar e gerenciar a pipeline completa de ticks
para cada símbolo.

Garante:

- Instância única por símbolo
- Encadeamento correto dos componentes
"""

from ..marketdata.tick_engine import TickEngine
from ..marketdata.tick_bus import TickBus
from ..marketdata.tick_writer import TickWriter
from ..marketdata.tick_repository import TickRepository
from ..marketdata.trade_tick_filter import TradeTickFilter

_engine_instances = {}


def ensure_tick_engine(symbol):
    """
    Retorna (ou cria) um TickEngine para o símbolo.

    Parameters
    ----------
    symbol : str

    Returns
    -------
    TickEngine
    """

    if symbol in _engine_instances:
        return _engine_instances[symbol]

    repo = TickRepository()

    raw_bus = TickBus()
    trade_bus = TickBus()

    raw_bus.subscribe(TradeTickFilter(trade_bus))

    writer = TickWriter(symbol, repo)
    trade_bus.subscribe(writer)

    engine = TickEngine(symbol, raw_bus)

    # 🔥 vínculo para shutdown
    engine.writer = writer

    _engine_instances[symbol] = engine

    return engine

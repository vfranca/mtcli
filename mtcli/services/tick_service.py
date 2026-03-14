"""
Tick Service

Responsável por inicializar e gerenciar o TickEngine
e seus componentes associados.

Arquitetura:

TickEngine
    ↓
TickBus
    ↓
Subscribers (TickWriter, plugins, etc)
"""

import logging

from mtcli.marketdata.tick_engine import TickEngine
from mtcli.marketdata.tick_bus import TickBus
from mtcli.marketdata.tick_writer import TickWriter
from mtcli.marketdata.tick_repository import TickRepository


logger = logging.getLogger(__name__)

_engine = None


def ensure_tick_engine(symbol: str):
    """
    Inicializa o TickEngine caso ainda não exista.

    Parameters
    ----------
    symbol : str
        Símbolo a capturar.

    Returns
    -------
    TickEngine
    """

    global _engine

    if _engine is not None:
        logger.debug("TickEngine já inicializado")
        return _engine

    logger.info("Inicializando TickEngine para %s", symbol)

    # ---------------------------------------------------------
    # Cria Event Bus
    # ---------------------------------------------------------

    tick_bus = TickBus()

    # ---------------------------------------------------------
    # Repository
    # ---------------------------------------------------------

    repository = TickRepository()

    # ---------------------------------------------------------
    # Writer subscriber
    # ---------------------------------------------------------

    writer = TickWriter(repository)

    tick_bus.subscribe(writer)

    # ---------------------------------------------------------
    # Engine
    # ---------------------------------------------------------

    _engine = TickEngine(
        symbol=symbol,
        tick_bus=tick_bus,
    )

    logger.info("TickEngine inicializado")

    return _engine

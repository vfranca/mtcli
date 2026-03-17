"""
TickBus

Event Bus simples para distribuição de ticks.
"""

from mtcli.logger import setup_logger

logger = setup_logger(__name__)


class TickBus:
    """
    Event bus simples para distribuição de ticks.
    """

    def __init__(self):

        self.subscribers = []

    # ---------------------------------------------------------

    def subscribe(self, handler):

        self.subscribers.append(handler)

        name = getattr(handler, "__qualname__", handler.__class__.__name__)

        logger.debug("Subscriber registrado: %s", name)

    # ---------------------------------------------------------

    def publish_many(self, ticks):

        for handler in self.subscribers:

            try:
                handler(ticks)

            except Exception:
                logger.exception("Erro em subscriber")

"""
TickBus

Event Bus simples para distribuição de ticks.
"""

from mtcli.logger import setup_logger

logger = setup_logger(__name__)


class TickBus:
    """
    Implementa um Event Bus simples para ticks.
    """

    def __init__(self):
        self.subscribers = []

    # ---------------------------------------------------------

    def subscribe(self, handler):
        """
        Registra um subscriber para receber ticks.
        """

        self.subscribers.append(handler)

        name = getattr(handler, "__qualname__", handler.__class__.__name__)

        logger.debug("Subscriber registrado: %s", name)

    # ---------------------------------------------------------

    def publish(self, tick):
        """
        Publica um único tick para todos os subscribers.
        """

        for handler in self.subscribers:
            try:
                handler(tick)

            except Exception:
                logger.exception("Erro em subscriber")

    # ---------------------------------------------------------

    def publish_many(self, ticks):
        """
        Publica um lote de ticks para todos os subscribers.

        Usado principalmente por mecanismos de backfill.
        """

        for handler in self.subscribers:
            try:
                handler(ticks)

            except Exception:
                logger.exception("Erro em subscriber")

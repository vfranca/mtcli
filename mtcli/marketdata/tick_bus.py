"""
TickBus

Event bus assíncrono baseado em fila.

Responsável por desacoplar produção e consumo de ticks.
"""

from queue import Queue, Full
import threading

from ..logger import setup_logger

logger = setup_logger(__name__)


class TickBus:

    def __init__(self, maxsize=10000):

        self.subscribers = []
        self.queue = Queue(maxsize=maxsize)

        self.worker = threading.Thread(
            target=self._loop,
            daemon=True
        )
        self.worker.start()

    def subscribe(self, handler):
        """Registra subscriber."""
        self.subscribers.append(handler)

    def publish_many(self, ticks):
        """Publica ticks na fila."""
        try:
            self.queue.put_nowait(ticks)
        except Full:
            logger.warning("TickBus cheio")

    def _loop(self):
        """Loop de dispatch."""
        while True:
            ticks = self.queue.get()

            for handler in self.subscribers:
                try:
                    handler(ticks)
                except Exception:
                    logger.exception("Erro subscriber")

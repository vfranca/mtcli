"""
TickWriter

Subscriber responsável por persistir ticks no banco.

Características:

- Processamento assíncrono via fila
- Batching por volume e tempo
- Flush manual (obrigatório para backfill)
- Thread dedicada

Garantias:

- Não bloqueia o pipeline
- Alta performance de escrita
- Controle explícito de consistência
"""

import threading
import time
from queue import Queue, Full, Empty

from ..logger import setup_logger

logger = setup_logger(__name__)


class TickWriter:

    def __init__(
        self,
        symbol,
        repository,
        batch_size=1000,
        flush_interval=0.5,
        queue_size=50000,
    ):
        self.symbol = symbol
        self.repository = repository

        self.queue = Queue(maxsize=queue_size)

        self.batch_size = batch_size
        self.flush_interval = flush_interval

        self.running = True
        self._buffer = []

        self.worker = threading.Thread(
            target=self._loop,
            daemon=True
        )
        self.worker.start()

    # ---------------------------------------------------------

    def __call__(self, ticks):
        try:
            self.queue.put(ticks, timeout=0.1)  # 🔥 backpressure real
        except Full:
            logger.warning("DROP %d ticks (%s)", len(ticks), self.symbol)

    # ---------------------------------------------------------

    def _loop(self):

        last_flush = time.time()

        while self.running:

            try:
                ticks = self.queue.get(timeout=0.1)
                self._buffer.extend(ticks)
            except Empty:
                pass

            now = time.time()

            if (
                len(self._buffer) >= self.batch_size
                or (self._buffer and (now - last_flush) >= self.flush_interval)
            ):
                self._flush()
                last_flush = now

        # flush final
        if self._buffer:
            self._flush()

    # ---------------------------------------------------------

    def _flush(self):

        try:
            conn = self.repository.conn

            conn.execute("BEGIN")

            inserted = self.repository.insert_ticks(
                self.symbol,
                self._buffer
            )

            conn.commit()

            # 🔥 atualiza cache no live
            self.repository.cache.add_many(self._buffer)

            logger.debug("Flush %d ticks (%s)", inserted, self.symbol)

        except Exception:
            conn.rollback()
            logger.exception("Erro no flush")

        finally:
            self._buffer.clear()

    # ---------------------------------------------------------

    def stop(self):
        self.running = False

    def join(self):
        self.worker.join()

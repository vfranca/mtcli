"""
TickWriter

Thread dedicada para escrita de ticks no SQLite.
Recebe ticks via TickBus e grava em batches grandes.
"""

import threading
from queue import Queue, Empty


class TickWriter:

    FLUSH_INTERVAL = 0.2
    MAX_BATCH = 5000

    def __init__(self, repositories):

        self.repositories = repositories
        self.queue = Queue(maxsize=100000)

        self.running = False
        self.thread = None

    # -----------------------------------------------------

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._run,
            daemon=True,
            name="mtcli-tick-writer"
        )

        self.thread.start()

    # -----------------------------------------------------

    def stop(self):

        self.running = False

        if self.thread:
            self.thread.join()

    # -----------------------------------------------------

    def push(self, symbol, ticks):

        self.queue.put((symbol, ticks))

    # -----------------------------------------------------

    def _run(self):

        buffers = {}

        while self.running:

            try:

                symbol, ticks = self.queue.get(timeout=self.FLUSH_INTERVAL)

                buffers.setdefault(symbol, []).extend(ticks)

                if len(buffers[symbol]) >= self.MAX_BATCH:
                    self._flush(symbol, buffers)

            except Empty:

                for symbol in list(buffers.keys()):
                    self._flush(symbol, buffers)

    # -----------------------------------------------------

    def _flush(self, symbol, buffers):

        ticks = buffers.get(symbol)

        if not ticks:
            return

        repo = self.repositories[symbol]

        repo.conn.execute("BEGIN")

        try:

            repo._insert_ticks(symbol, ticks)

            repo.cache.add_many(ticks)

            repo.conn.commit()

        except Exception:

            repo.conn.rollback()
            raise

        buffers[symbol] = []

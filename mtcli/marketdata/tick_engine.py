"""
TickEngine

Motor de captura contínua de ticks.
"""

import time
import threading
import MetaTrader5 as mt5

from datetime import datetime

from mtcli.mt5_context import mt5_conexao
from .tick_repository import TickRepository
from .tick_writer import TickWriter
from .tick_bus import TickBus


class TickEngine:

    POLL_INTERVAL = 0.05
    BATCH_SIZE = 1000
    OVERLAP_MS = 20

    def __init__(self, symbols):

        self.symbols = symbols

        self.tick_bus = TickBus()

        self.repositories = {
            symbol: TickRepository()
            for symbol in symbols
        }

        self.writer = TickWriter(self.repositories)

        # writer escuta o bus
        self.tick_bus.subscribe(self.writer.push)

        self.running = False
        self.thread = None

    # -----------------------------------------------------

    def start(self):

        if self.running:
            return

        self.running = True

        self.writer.start()

        self.thread = threading.Thread(
            target=self._run,
            daemon=True,
            name="mtcli-tick-engine",
        )

        self.thread.start()

    # -----------------------------------------------------

    def stop(self):

        self.running = False

        if self.thread:
            self.thread.join()

        self.writer.stop()

    # -----------------------------------------------------

    def _run(self):

        with mt5_conexao():

            last_positions = {}

            for symbol in self.symbols:

                repo = self.repositories[symbol]

                repo.sync(symbol)

                last_msc = repo._get_last_tick_msc(symbol)

                if last_msc:
                    last_positions[symbol] = last_msc
                else:
                    last_positions[symbol] = int(time.time() * 1000)

            while self.running:

                for symbol in self.symbols:
                    self._drain_symbol(symbol, last_positions)

                time.sleep(self.POLL_INTERVAL)

    # -----------------------------------------------------

    def _drain_symbol(self, symbol, last_positions):

        last_msc = last_positions[symbol]

        start_dt = datetime.fromtimestamp(
            (last_msc - self.OVERLAP_MS) * 0.001
        )

        while True:

            ticks = mt5.copy_ticks_from(
                symbol,
                start_dt,
                self.BATCH_SIZE,
                mt5.COPY_TICKS_ALL,
            )

            if ticks is None or len(ticks) == 0:
                break

            # publica ticks para todos os subscribers
            self.tick_bus.publish(symbol, ticks)

            last_msc = int(ticks[-1]["time_msc"])

            last_positions[symbol] = last_msc + 1

            start_dt = datetime.fromtimestamp(
                (last_msc - self.OVERLAP_MS) * 0.001
            )

            if len(ticks) < self.BATCH_SIZE:
                break

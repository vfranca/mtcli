"""
Motor de captura de ticks multi-ativo.
"""

import time
import threading
import MetaTrader5 as mt5
from datetime import datetime

from mtcli.mt5_context import mt5_conexao
from .tick_repository import TickRepository


class TickEngine:

    POLL_INTERVAL = 0.2

    def __init__(self, symbols):

        self.symbols = symbols

        self.repositories = {
            symbol: TickRepository()
            for symbol in symbols
        }

        self.running = False

    def start(self):

        thread = threading.Thread(
            target=self._run,
            daemon=True
        )

        self.running = True
        thread.start()

    def stop(self):

        self.running = False

    def _run(self):

        with mt5_conexao():

            last_positions = {}

            for symbol in self.symbols:

                repo = self.repositories[symbol]
                last_msc = repo._get_last_tick_msc(symbol)

                if last_msc:
                    last_positions[symbol] = last_msc + 1
                else:
                    last_positions[symbol] = int(time.time() * 1000)

            while self.running:

                for symbol in self.symbols:

                    repo = self.repositories[symbol]

                    start = last_positions[symbol]

                    ticks = mt5.copy_ticks_from(
                        symbol,
                        datetime.fromtimestamp(start / 1000),
                        1000,
                        mt5.COPY_TICKS_ALL
                    )

                    if ticks is None or len(ticks) == 0:
                        continue

                    repo.conn.execute("BEGIN")

                    try:

                        repo._insert_ticks(symbol, ticks)

                        repo.cache.add_many(ticks)

                        repo.conn.commit()

                    except Exception:

                        repo.conn.rollback()

                    last_positions[symbol] = int(ticks[-1]["time_msc"]) + 1

                time.sleep(self.POLL_INTERVAL)

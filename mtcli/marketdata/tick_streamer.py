"""
Captura contínua de ticks.

Objetivo:

- eliminar dependência do histórico do broker
- manter histórico próprio
"""

import time
import MetaTrader5 as mt5
from datetime import datetime

from mtcli.mt5_context import mt5_conexao
from .tick_repository import TickRepository


class TickStreamer:

    def __init__(self, symbol):

        self.symbol = symbol
        self.repo = TickRepository()

        self.running = False

    def start(self):
        """
        Inicia captura contínua de ticks.
        """

        self.running = True

        with mt5_conexao():

            last_msc = self.repo._get_last_tick_msc(self.symbol)

            if last_msc:
                start = last_msc + 1
            else:
                start = int(time.time() * 1000)

            while self.running:

                ticks = mt5.copy_ticks_from(
                    self.symbol,
                    datetime.fromtimestamp(start / 1000),
                    1000,
                    mt5.COPY_TICKS_ALL,
                )

                if ticks is None or len(ticks) == 0:

                    time.sleep(0.1)
                    continue

                self.repo.conn.execute("BEGIN")

                try:

                    self.repo._insert_ticks(self.symbol, ticks)

                    self.repo.cache.add_many(ticks)

                    self.repo.conn.commit()

                except Exception:

                    self.repo.conn.rollback()

                start = int(ticks[-1]["time_msc"]) + 1

    def stop(self):

        self.running = False

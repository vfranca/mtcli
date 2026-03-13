"""
TickEngine - motor de captura contínua de ticks.

Responsável por:

- sincronizar histórico inicial
- capturar ticks em tempo real
- enviar ticks para o TickWriter
- manter posição de leitura por símbolo
"""

import time
import threading
import MetaTrader5 as mt5

from datetime import datetime

from mtcli.mt5_context import mt5_conexao
from .tick_repository import TickRepository
from .tick_writer import TickWriter


class TickEngine:

    # intervalo entre ciclos de polling
    POLL_INTERVAL = 0.05

    # tamanho máximo retornado pelo MT5
    BATCH_SIZE = 1000

    # sobreposição para evitar perda de ticks
    OVERLAP_MS = 20

    def __init__(self, symbols):

        self.symbols = symbols

        # repositórios por símbolo
        self.repositories = {
            symbol: TickRepository()
            for symbol in symbols
        }

        # writer assíncrono
        self.writer = TickWriter(self.repositories)

        self.running = False
        self.thread = None

    # ==========================================================
    # CONTROLE DO ENGINE
    # ==========================================================

    def start(self):
        """
        Inicia o motor de captura.
        """

        if self.running:
            return

        self.running = True

        # inicia writer
        self.writer.start()

        self.thread = threading.Thread(
            target=self._run,
            daemon=True,
            name="mtcli-tick-engine",
        )

        self.thread.start()

    def stop(self):
        """
        Interrompe captura de ticks.
        """

        self.running = False

        if self.thread:
            self.thread.join()

        # garante flush final
        self.writer.stop()

    # ==========================================================
    # LOOP PRINCIPAL
    # ==========================================================

    def _run(self):

        with mt5_conexao():

            last_positions = {}

            # --------------------------------------------------
            # sincronização inicial
            # --------------------------------------------------

            for symbol in self.symbols:

                repo = self.repositories[symbol]

                repo.sync(symbol)

                last_msc = repo._get_last_tick_msc(symbol)

                if last_msc:
                    last_positions[symbol] = last_msc
                else:
                    last_positions[symbol] = int(time.time() * 1000)

            # --------------------------------------------------
            # loop contínuo
            # --------------------------------------------------

            while self.running:

                for symbol in self.symbols:
                    self._drain_symbol(symbol, last_positions)

                time.sleep(self.POLL_INTERVAL)

    # ==========================================================
    # CAPTURA POR SÍMBOLO
    # ==========================================================

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

            # envia ticks para o writer assíncrono
            self.writer.push(symbol, ticks)

            last_msc = int(ticks[-1]["time_msc"])

            last_positions[symbol] = last_msc + 1

            start_dt = datetime.fromtimestamp(
                (last_msc - self.OVERLAP_MS) * 0.001
            )

            if len(ticks) < self.BATCH_SIZE:
                break

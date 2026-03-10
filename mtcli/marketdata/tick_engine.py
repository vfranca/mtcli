"""
TickEngine - motor de captura contínua de ticks.

Responsável por coletar ticks diretamente do MetaTrader 5
e persistir os dados no banco SQLite do mtcli.

Características:

- captura multi-símbolo
- ingestão contínua de dados
- proteção contra perda de ticks via overlap
- drenagem completa do buffer do MT5
- gravação otimizada em SQLite (WAL)

Fluxo de dados:

    MetaTrader 5
        ↓
    TickEngine
        ↓
    TickRepository
        ↓
    SQLite (WAL)

O engine mantém um cursor por símbolo baseado em
`time_msc` (timestamp em milissegundos), garantindo
que nenhum tick seja perdido.

Para evitar lacunas causadas por latência, um pequeno
overlap é aplicado ao consultar novos ticks.
"""

import time
import threading
import MetaTrader5 as mt5

from datetime import datetime

from mtcli.mt5_context import mt5_conexao
from .tick_repository import TickRepository


class TickEngine:
    """
    Motor de captura de ticks multi-símbolo.
    """

    POLL_INTERVAL = 0.2
    BATCH_SIZE = 1000
    OVERLAP_MS = 5

    def __init__(self, symbols):
        """
        Inicializa o engine.

        Args:
            symbols (list[str]):
                Lista de símbolos a serem monitorados.
        """

        self.symbols = symbols

        self.repositories = {
            symbol: TickRepository()
            for symbol in symbols
        }

        self.running = False
        self.thread = None

    def start(self):
        """
        Inicia o engine em uma thread dedicada.
        """

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self._run,
            daemon=True,
            name="mtcli-tick-engine",
        )

        self.thread.start()

    def stop(self):
        """
        Encerra o engine de captura de ticks.
        """

        self.running = False

        if self.thread:
            self.thread.join()

    def _run(self):
        """
        Loop principal de captura.
        """

        with mt5_conexao():

            last_positions = {}

            for symbol in self.symbols:

                repo = self.repositories[symbol]

                last_msc = repo._get_last_tick_msc(symbol)

                if last_msc:
                    last_positions[symbol] = last_msc
                else:
                    last_positions[symbol] = int(time.time() * 1000)

            while self.running:

                for symbol in self.symbols:

                    self._drain_symbol(symbol, last_positions)

                time.sleep(self.POLL_INTERVAL)

    def _drain_symbol(self, symbol, last_positions):
        """
        Consome todos os ticks disponíveis para um símbolo.

        Esse método garante que picos de mercado não causem
        perda de ticks, drenando completamente o buffer
        retornado pela API do MetaTrader.

        Args:
            symbol (str):
                Símbolo a ser processado.

            last_positions (dict):
                Cursor de posição por símbolo.
        """

        repo = self.repositories[symbol]

        last_msc = last_positions[symbol]

        start_dt = datetime.fromtimestamp(
            (last_msc - self.OVERLAP_MS) / 1000
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

            repo.conn.execute("BEGIN")

            try:

                repo._insert_ticks(symbol, ticks)

                repo.cache.add_many(ticks)

                repo.conn.commit()

            except Exception:

                repo.conn.rollback()
                raise

            last_msc = int(ticks[-1]["time_msc"])

            last_positions[symbol] = last_msc + 1

            start_dt = datetime.fromtimestamp(
                (last_msc - self.OVERLAP_MS) / 1000
            )

            if len(ticks) < self.BATCH_SIZE:
                break

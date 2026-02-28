"""
TickRepository profissional com:

- Paginação automática
- Sincronização incremental robusta
- Integração com mt5_conexao
- Proteção contra loops infinitos
"""

import MetaTrader5 as mt5
from datetime import datetime, timedelta

from ..database import get_connection
from .tick_cache import TickCache
from mtcli.mt5_context import mt5_conexao


class TickRepository:

    BATCH_SIZE = 200000  # tamanho seguro por lote

    def __init__(self):
        self.conn = get_connection()
        self.cache = TickCache()

    # ============================================================
    # SINCRONIZAÇÃO COM PAGINAÇÃO
    # ============================================================

    def sync(self, symbol: str, days_back: int = 1):
        """
        Sincroniza banco com MT5 usando paginação.

        Busca todos os ticks disponíveis desde o último timestamp.
        """

        total_inserted = 0

        with mt5_conexao():

            last_time = self._get_last_tick_time(symbol)

            if last_time:
                start = datetime.fromtimestamp(last_time + 1)
            else:
                start = datetime.now() - timedelta(days=days_back)

            while True:

                ticks = mt5.copy_ticks_from(
                    symbol,
                    start,
                    self.BATCH_SIZE,
                    mt5.COPY_TICKS_ALL,
                )

                if ticks is None or len(ticks) == 0:
                    break

                inserted = self._insert_ticks(symbol, ticks)
                total_inserted += inserted

                self.cache.add_many(ticks)

                # Atualiza início para próximo tick
                ultimo_timestamp = int(ticks[-1]["time"])
                novo_start = datetime.fromtimestamp(ultimo_timestamp + 1)

                # Proteção contra loop infinito
                if novo_start <= start:
                    break

                start = novo_start

                # Se retornou menos que o batch, acabou histórico
                if len(ticks) < self.BATCH_SIZE:
                    break

        return total_inserted

    # ============================================================
    # INSERÇÃO
    # ============================================================

    def _insert_ticks(self, symbol, ticks):

        cursor = self.conn.cursor()

        data = [
            (
                symbol,
                int(t["time"]),
                float(t["bid"]),
                float(t["ask"]),
                float(t["last"]),
                float(t["volume"]),
                int(t["flags"]),
            )
            for t in ticks
        ]

        cursor.executemany(
            """
            INSERT OR IGNORE INTO ticks
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            data,
        )

        self.conn.commit()
        return cursor.rowcount

    # ============================================================
    # CONSULTAS
    # ============================================================

    def get_ticks_between(self, symbol, start_ts, end_ts):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT time, bid, ask, last, volume, flags
            FROM ticks
            WHERE symbol = ?
            AND time BETWEEN ? AND ?
            ORDER BY time ASC
            """,
            (symbol, start_ts, end_ts),
        )
        return cursor.fetchall()

    def _get_last_tick_time(self, symbol):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT MAX(time)
            FROM ticks
            WHERE symbol = ?
            """,
            (symbol,),
        )
        result = cursor.fetchone()
        return result[0] if result and result[0] else None

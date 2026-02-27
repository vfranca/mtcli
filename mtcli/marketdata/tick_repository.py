"""
TickRepository centralizado.

Responsável por:
- Sincronizar com MT5 via mt5_conexao
- Persistir ticks corretamente (structured array numpy)
- Fornecer ticks para modelos
"""

import MetaTrader5 as mt5
from datetime import datetime, timedelta

from ..database import get_connection
from .tick_cache import TickCache
from mtcli.mt5_context import mt5_conexao


class TickRepository:

    def __init__(self):
        self.conn = get_connection()
        self.cache = TickCache()

    # ============================================================
    # SINCRONIZAÇÃO INCREMENTAL
    # ============================================================

    def sync(self, symbol: str, days_back: int = 1):
        """
        Sincroniza banco com MT5.

        Busca apenas ticks após o último armazenado.
        """

        with mt5_conexao():

            last_time = self._get_last_tick_time(symbol)

            if last_time:
                start = datetime.fromtimestamp(last_time)
            else:
                start = datetime.now() - timedelta(days=days_back)

            ticks = mt5.copy_ticks_from(
                symbol,
                start,
                200000,
                mt5.COPY_TICKS_ALL,
            )

            if ticks is None or len(ticks) == 0:
                return 0

            inserted = self._insert_ticks(symbol, ticks)
            self.cache.add_many(ticks)

            return inserted

    # ============================================================
    # INSERÇÃO
    # ============================================================

    def _insert_ticks(self, symbol, ticks):
        """
        Insere ticks no SQLite.

        O retorno do MT5 é numpy structured array.
        Acesso deve ser por campo: t["time"], t["last"], etc.
        """

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

"""
TickRepository profissional.

Responsável por:

- Persistir ticks no SQLite
- Sincronizar histórico inicial
"""

import MetaTrader5 as mt5
from datetime import datetime, timedelta

from ..database import get_connection, wal_checkpoint, backup_database
from .tick_cache import TickCache
from mtcli.mt5_context import mt5_conexao


class TickRepository:

    BATCH_SIZE = 200000

    def __init__(self):

        self.conn = get_connection()
        self.cache = TickCache()

        self.insert_counter = 0
        self.last_backup_day = None

    # ==========================================================
    # SINCRONIZAÇÃO HISTÓRICA
    # ==========================================================

    def sync(self, symbol: str, days_back: int = 1):

        total_inserted = 0

        with mt5_conexao():

            last_msc = self._get_last_tick_msc(symbol)

            if last_msc:
                start = datetime.fromtimestamp(last_msc / 1000)
            else:
                start = datetime.now() - timedelta(days=days_back)

            self.conn.execute("BEGIN")

            try:

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

                    last_msc = int(ticks[-1]["time_msc"])

                    start = datetime.fromtimestamp(last_msc / 1000)

                    if len(ticks) < self.BATCH_SIZE:
                        break

                self.conn.commit()

            except Exception:

                self.conn.rollback()
                raise

        return total_inserted

    # ==========================================================
    # INSERÇÃO
    # ==========================================================

    def _insert_ticks(self, symbol, ticks):

        cursor = self.conn.cursor()

        data = [
            (
                symbol,
                int(t["time"]),
                int(t["time_msc"]),
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
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            data,
        )

        inserted = cursor.rowcount

        self.insert_counter += inserted

        # checkpoint periódico
        if self.insert_counter >= 200000:

            wal_checkpoint(self.conn)
            self.insert_counter = 0

        # backup diário
        today = datetime.now().date()

        if self.last_backup_day != today:

            backup_database(self.conn)
            self.last_backup_day = today

        return inserted

    # ==========================================================
    # CONSULTAS
    # ==========================================================

    def get_ticks_between(self, symbol, start_msc, end_msc):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT time_msc, bid, ask, last, volume, flags
            FROM ticks
            WHERE symbol = ?
            AND time_msc BETWEEN ? AND ?
            ORDER BY time_msc ASC
            """,
            (symbol, start_msc, end_msc),
        )

        return cursor.fetchall()

    # ==========================================================
    # UTILITÁRIOS
    # ==========================================================

    def _get_last_tick_msc(self, symbol):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT MAX(time_msc)
            FROM ticks
            WHERE symbol = ?
            """,
            (symbol,),
        )

        result = cursor.fetchone()

        return result[0] if result and result[0] else None

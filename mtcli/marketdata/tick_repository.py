"""
TickRepository.

Responsável por:

- Persistir ticks no SQLite
- Sincronizar histórico inicial
- Consultas rápidas para engines
"""

import MetaTrader5 as mt5
from datetime import datetime, timedelta

from ..database import get_connection, backup_database
from .tick_cache import TickCache
from mtcli.mt5_context import mt5_conexao


class TickRepository:

    BATCH_SIZE = 200000

    def __init__(self):

        self.conn = get_connection()
        self.cache = TickCache()

        self.last_backup_day = None

    # ==========================================================
    # SINCRONIZAÇÃO HISTÓRICA
    # ==========================================================

    def sync(self, symbol: str, days_back: int = 1):

        total_inserted = 0

        with mt5_conexao():

            last_msc = self._get_last_tick_msc(symbol)

            if last_msc:
                start = datetime.fromtimestamp((last_msc + 1) / 1000)
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

                    start = datetime.fromtimestamp((last_msc + 1) / 1000)

                    if len(ticks) < self.BATCH_SIZE:
                        break

                self.conn.commit()

            except Exception:

                self.conn.rollback()
                raise

        self._daily_backup()

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
            INSERT INTO ticks(
                symbol,time,time_msc,bid,ask,last,volume,flags
            )
            VALUES (?,?,?,?,?,?,?,?)
            ON CONFLICT(symbol,time) DO NOTHING
            """,
            data,
        )

        return len(data)

    # ==========================================================
    # CONSULTAS
    # ==========================================================

    def get_last_ticks(self, symbol, limit=5000):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT time_msc,bid,ask,last,volume,flags
            FROM ticks
            WHERE symbol = ?
            ORDER BY time_msc DESC
            LIMIT ?
            """,
            (symbol, limit),
        )

        rows = cursor.fetchall()

        rows.reverse()

        return rows

    def get_ticks_between(self, symbol, start_msc, end_msc):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT time_msc,bid,ask,last,volume,flags
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

    def _daily_backup(self):

        today = datetime.now().date()

        if self.last_backup_day != today:

            backup_database(self.conn)
            self.last_backup_day = today

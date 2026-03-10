"""
TickRepository.

Responsável por:

- persistência de ticks
- sincronização histórica
- consultas rápidas
"""

import MetaTrader5 as mt5

from datetime import datetime, timedelta

from ..database import get_connection, backup_database
from .tick_cache import TickCache
from mtcli.mt5_context import mt5_conexao


class TickRepository:

    RANGE_WINDOW_MINUTES = 10

    def __init__(self):

        self.conn = get_connection()
        self.cache = TickCache()

        self.last_backup_day = None

    # ==========================================================
    # SYNC HISTÓRICO
    # ==========================================================

    def sync(self, symbol: str, days_back: int = 1):

        total_inserted = 0

        end = datetime.now()

        last_msc = self._get_last_tick_msc(symbol)

        if last_msc:
            start = datetime.fromtimestamp((last_msc + 1) / 1000)
        else:
            start = end - timedelta(days=days_back)

        window = timedelta(minutes=self.RANGE_WINDOW_MINUTES)

        with mt5_conexao():

            while start < end:

                chunk_end = min(start + window, end)

                ticks = mt5.copy_ticks_range(
                    symbol,
                    start,
                    chunk_end,
                    mt5.COPY_TICKS_ALL
                )

                if ticks is not None and len(ticks) > 0:

                    self.conn.execute("BEGIN")

                    try:

                        inserted = self._insert_ticks(symbol, ticks)

                        total_inserted += inserted

                        self.cache.add_many(ticks)

                        self.conn.commit()

                    except Exception:

                        self.conn.rollback()
                        raise

                start = chunk_end

        self._daily_backup()

        return total_inserted

    # ==========================================================
    # INSERT
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
            ON CONFLICT(symbol,time_msc) DO NOTHING
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
    # UTIL
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

        row = cursor.fetchone()

        return row[0] if row and row[0] else None

    def _daily_backup(self):

        today = datetime.now().date()

        if self.last_backup_day != today:

            backup_database(self.conn)
            self.last_backup_day = today

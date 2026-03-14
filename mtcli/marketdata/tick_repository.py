"""
TickRepository

Responsável por:

- persistência de ticks
- sincronização histórica
- consultas rápidas
- backup automático
- política opcional de retenção

Implementa compressão de preços:

preço_real = preço_armazenado / PRICE_SCALE
"""

import MetaTrader5 as mt5

from datetime import datetime, timedelta

from ..database import get_connection, backup_database
from .tick_cache import TickCache
from mtcli.mt5_context import mt5_conexao


class TickRepository:

    # -----------------------------------------------------
    # CONFIGURAÇÕES
    # -----------------------------------------------------

    RANGE_WINDOW_MINUTES = 10
    PRICE_SCALE = 100

    # retenção opcional
    TICK_RETENTION_DAYS = 30

    def __init__(self):

        self.conn = get_connection()

        self.cache = TickCache()

        self.last_backup_day = None
        self.last_purge_day = None

    # =====================================================
    # SYNC HISTÓRICO
    # =====================================================

    def sync(self, symbol: str, days_back: int = 1):
        """
        Sincroniza histórico inicial de ticks.

        Busca dados históricos no MT5 e grava
        no banco em janelas de tempo.
        """

        total_inserted = 0

        end = datetime.now()

        last_msc = self._get_last_tick_msc(symbol)

        if last_msc:
            start = datetime.fromtimestamp((last_msc + 1) * 0.001)
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
        self._daily_purge()

        return total_inserted

    # =====================================================
    # INSERT
    # =====================================================

    def _insert_ticks(self, symbol, ticks):
        """
        Insere ticks no banco.

        Utiliza INSERT OR IGNORE para evitar duplicações.
        """

        scale = self.PRICE_SCALE

        data = [
            (
                symbol,
                int(t["time_msc"]),
                int(t["bid"] * scale),
                int(t["ask"] * scale),
                int(t["last"] * scale),
                int(t["volume"]),
                int(t["flags"]),
            )
            for t in ticks
        ]

        cursor = self.conn.executemany(
            """
            INSERT OR IGNORE INTO ticks(
                symbol,
                time_msc,
                bid,
                ask,
                last,
                volume,
                flags
            )
            VALUES (?,?,?,?,?,?,?)
            """,
            data,
        )

        return cursor.rowcount

    # =====================================================
    # CONSULTAS
    # =====================================================

    def get_last_ticks(self, symbol, limit=5000):
        """
        Retorna últimos ticks de um símbolo.
        """

        rows = self.conn.execute(
            """
            SELECT time_msc,bid,ask,last,volume,flags
            FROM ticks
            WHERE symbol = ?
            ORDER BY time_msc DESC
            LIMIT ?
            """,
            (symbol, limit),
        ).fetchall()

        if not rows:
            return []

        rows.reverse()

        scale = self.PRICE_SCALE

        return [
            (
                r[0],
                r[1] / scale,
                r[2] / scale,
                r[3] / scale,
                r[4],
                r[5],
            )
            for r in rows
        ]

    # -----------------------------------------------------

    def get_ticks_between(self, symbol, start_msc, end_msc):
        """
        Retorna ticks entre dois timestamps.
        """

        rows = self.conn.execute(
            """
            SELECT time_msc,bid,ask,last,volume,flags
            FROM ticks
            WHERE symbol = ?
            AND time_msc BETWEEN ? AND ?
            ORDER BY time_msc ASC
            """,
            (symbol, start_msc, end_msc),
        ).fetchall()

        if not rows:
            return []

        scale = self.PRICE_SCALE

        return [
            (
                r[0],
                r[1] / scale,
                r[2] / scale,
                r[3] / scale,
                r[4],
                r[5],
            )
            for r in rows
        ]

    # =====================================================
    # UTIL
    # =====================================================

    def _get_last_tick_msc(self, symbol):
        """
        Retorna timestamp do último tick armazenado.
        """

        row = self.conn.execute(
            """
            SELECT MAX(time_msc)
            FROM ticks
            WHERE symbol = ?
            """,
            (symbol,),
        ).fetchone()

        return row[0] if row and row[0] else None

    # =====================================================
    # BACKUP AUTOMÁTICO
    # =====================================================

    def _daily_backup(self):

        today = datetime.now().date()

        if self.last_backup_day != today:

            backup_database(self.conn)

            self.last_backup_day = today

    # =====================================================
    # RETENÇÃO DE TICKS
    # =====================================================

    def _daily_purge(self):
        """
        Remove ticks antigos para evitar crescimento
        infinito do banco.
        """

        if self.TICK_RETENTION_DAYS <= 0:
            return

        today = datetime.now().date()

        if self.last_purge_day == today:
            return

        cutoff = int(
            (datetime.now() - timedelta(days=self.TICK_RETENTION_DAYS)).timestamp()
            * 1000
        )

        self.conn.execute(
            """
            DELETE FROM ticks
            WHERE time_msc < ?
            """,
            (cutoff,),
        )

        self.conn.commit()

        self.last_purge_day = today

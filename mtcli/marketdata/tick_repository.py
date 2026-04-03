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

from datetime import datetime, timedelta, timezone

from ..logger import setup_logger
from ..database import get_connection, backup_database
from .tick_cache import TickCache
from ..mt5_context import mt5_conexao
from ..utils.time import now_utc

logger = setup_logger(__name__)


class TickRepository:

    RANGE_WINDOW_MINUTES = 10
    PRICE_SCALE = 100

    TICK_RETENTION_DAYS = 30

    def __init__(self):

        self.conn = get_connection()

        self.cache = TickCache()

        self.last_backup_day = None
        self.last_purge_day = None

        logger.debug("TickRepository inicializado")

    # =====================================================
    # SYNC HISTÓRICO
    # =====================================================

    def sync(self, symbol: str, days_back: int = 1):

        logger.info("Iniciando sync histórico de ticks (%s)", symbol)

        total_inserted = 0

        end = now_utc()

        last_msc = self._get_last_tick_msc(symbol)

        if last_msc:
            start = datetime.fromtimestamp(
                (last_msc + 1) * 0.001,
                tz=timezone.utc
            )
            logger.debug("Continuando sync a partir de %s", start)
        else:
            start = end - timedelta(days=days_back)
            logger.debug("Sync inicial iniciando em %s", start)

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

                        logger.debug(
                            "Chunk sync: %d ticks inseridos (%s)",
                            inserted,
                            symbol
                        )

                    except Exception:

                        self.conn.rollback()

                        logger.exception("Erro durante sync de ticks")

                        raise

                start = chunk_end

        self._daily_backup()
        self._daily_purge()

        logger.info(
            "Sync histórico concluído (%s) — %d ticks inseridos",
            symbol,
            total_inserted
        )

        return total_inserted

    # =====================================================
    # INSERT
    # =====================================================

    def insert_ticks(self, symbol, ticks):

        if ticks is None or len(ticks) == 0:
            return 0

        logger.debug(
            "TickRepository inserindo %d ticks (%s)",
            len(ticks),
            symbol
        )

        scale = self.PRICE_SCALE

        data = [
            (
                symbol,
                int(t["time_msc"]),
                int(round(t["bid"] * scale)),
                int(round(t["ask"] * scale)),
                int(round(t["last"] * scale)),
                int(t["volume"]),
                int(t["flags"]),
            )
            for t in ticks
        ]

        cursor = self.conn.executemany(
            """
            INSERT OR IGNORE INTO ticks(
                symbol,time_msc,bid,ask,last,volume,flags
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

        logger.debug(
            "Consulta últimos %d ticks (%s)",
            limit,
            symbol
        )

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

    def get_ticks_between(self, symbol, start_msc, end_msc):

        logger.debug(
            "Consulta ticks entre %s e %s (%s)",
            start_msc,
            end_msc,
            symbol
        )

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

        row = self.conn.execute(
            """
            SELECT MAX(time_msc)
            FROM ticks
            WHERE symbol = ?
            """,
            (symbol,),
        ).fetchone()

        last = row[0] if row and row[0] else None

        logger.debug("Último tick armazenado (%s): %s", symbol, last)

        return last

    # =====================================================
    # BACKUP AUTOMÁTICO
    # =====================================================

    def _daily_backup(self):

        today = now_utc().date()

        if self.last_backup_day != today:

            logger.info("Executando backup automático do banco")

            backup_database(self.conn)

            self.last_backup_day = today

    # =====================================================
    # RETENÇÃO DE TICKS
    # =====================================================

    def _daily_purge(self):

        if self.TICK_RETENTION_DAYS <= 0:
            return

        today = now_utc().date()

        if self.last_purge_day == today:
            return

        cutoff = int(
            (now_utc() - timedelta(days=self.TICK_RETENTION_DAYS)).timestamp() * 1000
        )

        logger.info("Executando purge de ticks antigos")

        self.conn.execute(
            """
            DELETE FROM ticks
            WHERE time_msc < ?
            """,
            (cutoff,),
        )

        self.conn.commit()

        self.last_purge_day = today

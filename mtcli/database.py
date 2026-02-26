"""
Database core para mtcli.

Responsável por:
- Criar conexão SQLite
- Ativar WAL
- Garantir schema
"""

import sqlite3
from pathlib import Path


DB_PATH = Path.home() / ".mtcli" / "marketdata.db"


def get_connection():
    """
    Retorna conexão SQLite configurada.
    """
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")

    _ensure_schema(conn)
    return conn


def _ensure_schema(conn):
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS ticks (
            symbol TEXT NOT NULL,
            time INTEGER NOT NULL,
            bid REAL,
            ask REAL,
            last REAL,
            volume REAL,
            flags INTEGER,
            PRIMARY KEY (symbol, time)
        );
        """
    )

    conn.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_ticks_symbol_time
        ON ticks(symbol, time);
        """
    )

    conn.commit()

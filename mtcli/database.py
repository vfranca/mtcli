"""
Core de acesso ao banco SQLite do mtcli.

Responsável por:

- criar conexão SQLite
- aplicar otimizações
- executar migrations automaticamente
- backup automático
"""

import sqlite3
from pathlib import Path
from datetime import datetime

from .conf import DB_NAME
from .migrations.runner import run_migrations


DB_PATH = Path.home() / ".mtcli" / DB_NAME
BACKUP_DIR = Path.home() / ".mtcli" / "backups"

_connection = None


def get_connection():
    """
    Retorna conexão singleton SQLite.
    """

    global _connection

    if _connection:
        return _connection

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)

    # otimizações
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA temp_store=MEMORY")
    conn.execute("PRAGMA mmap_size=30000000000")
    conn.execute("PRAGMA cache_size=-200000")
    conn.execute("PRAGMA journal_size_limit=67108864")
    conn.execute("PRAGMA wal_autocheckpoint=5000")
    conn.execute("PRAGMA foreign_keys=ON")

    # executa migrations automaticamente
    run_migrations(conn)

    _connection = conn

    return conn


# ==========================================================
# BACKUP
# ==========================================================

def backup_database(conn):

    now = datetime.now().strftime("%Y%m%d")

    backup_path = BACKUP_DIR / f"marketdata_{now}.db"

    if backup_path.exists():
        return

    backup_conn = sqlite3.connect(backup_path)

    with backup_conn:
        conn.backup(backup_conn)

    backup_conn.close()

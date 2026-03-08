import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path.home() / ".mtcli" / "marketdata.db"
BACKUP_DIR = Path.home() / ".mtcli" / "backups"


def get_connection():

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)

    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA temp_store=MEMORY")
    conn.execute("PRAGMA mmap_size=30000000000")
    conn.execute("PRAGMA cache_size=-200000")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS schema_migrations(
        version INTEGER PRIMARY KEY,
        applied_at TEXT NOT NULL
    )
    """)

    conn.commit()

    return conn


# ==========================================================
# CHECKPOINT
# ==========================================================

def wal_checkpoint(conn):
    """
    Reduz tamanho do WAL e mantém banco saudável.
    """
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")


# ==========================================================
# BACKUP
# ==========================================================

def backup_database(conn):
    """
    Backup diário seguro do banco SQLite.
    """

    now = datetime.now().strftime("%Y%m%d")

    backup_path = BACKUP_DIR / f"marketdata_{now}.db"

    if backup_path.exists():
        return

    backup_conn = sqlite3.connect(backup_path)

    with backup_conn:
        conn.backup(backup_conn)

    backup_conn.close()

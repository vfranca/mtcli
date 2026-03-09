"""
Core de acesso ao banco SQLite do mtcli.

Responsável por:

- Criar conexão SQLite
- Aplicar otimizações de performance
- Ativar WAL
- Gerenciar migrations
- Backup e manutenção do banco
"""

import sqlite3
from pathlib import Path
from datetime import datetime
from .conf import DB_NAME

DB_PATH = Path.home() / ".mtcli" / DB_NAME
BACKUP_DIR = Path.home() / ".mtcli" / "backups"


def get_connection():
    """
    Cria ou retorna uma conexão SQLite otimizada para ingestão
    contínua de ticks de mercado.

    Configurações aplicadas:

    - WAL (Write Ahead Logging)
    - synchronous=NORMAL
    - temp_store em memória
    - mmap para leitura rápida
    - cache expandido

    Returns
    -------
    sqlite3.Connection
        Conexão ativa com o banco SQLite.
    """

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)

    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA temp_store=MEMORY")
    conn.execute("PRAGMA mmap_size=268435456")
    conn.execute("PRAGMA cache_size=-200000")
    conn.execute("PRAGMA journal_size_limit=67108864")

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
    Executa checkpoint do WAL.

    Move os dados do arquivo `.wal` para o banco principal
    e reduz seu tamanho.
    """

    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")


# ==========================================================
# BACKUP
# ==========================================================

def backup_database(conn):
    """
    Realiza backup diário seguro do banco SQLite.

    O backup utiliza a API nativa do SQLite,
    permitindo cópia consistente mesmo com o banco em uso.
    """

    now = datetime.now().strftime("%Y%m%d")

    backup_path = BACKUP_DIR / f"marketdata_{now}.db"

    if backup_path.exists():
        return

    backup_conn = sqlite3.connect(backup_path)

    with backup_conn:
        conn.backup(backup_conn)

    backup_conn.close()

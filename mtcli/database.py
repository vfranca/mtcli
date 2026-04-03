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
from .logger import setup_logger


# ==========================================================
# LOGGER
# ==========================================================

log = setup_logger(__name__)


# ==========================================================
# PATHS
# ==========================================================

DB_PATH = Path.home() / ".mtcli" / DB_NAME
BACKUP_DIR = Path.home() / ".mtcli" / "backups"

_connection = None


# ==========================================================
# CONNECTION
# ==========================================================

def get_connection():
    """
    Retorna conexão singleton SQLite.
    """

    global _connection

    if _connection:
        log.debug("Reutilizando conexão SQLite existente.")
        return _connection

    log.debug("Inicializando conexão SQLite.")

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    log.debug("Diretórios garantidos: db=%s backups=%s", DB_PATH.parent, BACKUP_DIR)

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)

    log.debug("Conexão SQLite criada em %s", DB_PATH)

    # ======================================================
    # PRAGMAS DE OTIMIZAÇÃO
    # ======================================================

    log.debug("Aplicando otimizações PRAGMA.")

    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA temp_store=MEMORY")
    conn.execute("PRAGMA mmap_size=30000000000")
    conn.execute("PRAGMA cache_size=-200000")
    conn.execute("PRAGMA journal_size_limit=67108864")
    conn.execute("PRAGMA wal_autocheckpoint=5000")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute("PRAGMA busy_timeout=5000")  # 🔥 novo

    log.debug("PRAGMAs aplicadas com sucesso.")

    # ======================================================
    # MIGRATIONS
    # ======================================================

    log.debug("Executando migrations do banco de dados.")

    try:
        run_migrations(conn)
        log.info("Migrations executadas/verificadas com sucesso.")
    except Exception:
        log.exception("Erro ao executar migrations.")
        raise

    _connection = conn

    log.debug("Conexão SQLite inicializada e armazenada como singleton.")

    return conn


# ==========================================================
# BACKUP
# ==========================================================

def backup_database(conn):
    """
    Cria backup diário do banco de dados SQLite.

    O backup é realizado apenas uma vez por dia.
    """

    now = datetime.now().strftime("%Y%m%d")

    backup_path = BACKUP_DIR / f"marketdata_{now}.db"

    log.debug("Verificando necessidade de backup diário: %s", backup_path)

    if backup_path.exists():
        log.debug("Backup diário já existe. Ignorando backup.")
        return

    log.info("Iniciando backup do banco para %s", backup_path)

    try:

        backup_conn = sqlite3.connect(backup_path)

        with backup_conn:
            conn.backup(backup_conn)

        backup_conn.close()

        log.info("Backup concluído com sucesso.")

    except Exception:
        log.exception("Falha durante backup do banco.")
        raise

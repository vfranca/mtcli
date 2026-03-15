"""
Migration Runner do mtcli.

Responsabilidades:

1. Descobrir migrations disponíveis no diretório `mtcli/migrations`
2. Determinar a versão atual do schema no banco
3. Executar migrations pendentes em ordem
4. Registrar migrations aplicadas na tabela `schema_migrations`

Formato obrigatório das migrations:

    NNN_nome_da_migration.py

Exemplo:

    001_initial_schema.py
    002_ticks_time_msc.py
    003_optimize_ticks_without_rowid.py

Cada migration deve implementar:

    def upgrade(conn)
"""

import importlib
from pathlib import Path

from ..logger import setup_logger


log = setup_logger(__name__)


MIGRATIONS_DIR = Path(__file__).parent
PACKAGE = "mtcli.migrations"


# ---------------------------------------------------------
# Infraestrutura
# ---------------------------------------------------------

def ensure_migrations_table(conn):
    """
    Garante que a tabela `schema_migrations` exista.

    Esta tabela armazena quais migrations já foram
    aplicadas no banco.
    """

    log.debug("Garantindo existência da tabela schema_migrations.")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS schema_migrations(
        version INTEGER PRIMARY KEY,
        applied_at TEXT NOT NULL
    )
    """)

    conn.commit()


# ---------------------------------------------------------
# Estado do banco
# ---------------------------------------------------------

def get_current_version(conn):
    """
    Retorna a versão atual do schema.

    Returns
    -------
    int
        Maior versão registrada em `schema_migrations`.
        Retorna 0 se nenhuma migration foi aplicada.
    """

    cursor = conn.execute(
        "SELECT MAX(version) FROM schema_migrations"
    )

    row = cursor.fetchone()

    version = row[0] if row and row[0] else 0

    log.debug("Versão atual do schema: %s", version)

    return version


def mark_version(conn, version):
    """
    Marca uma migration como aplicada.
    """

    log.debug("Registrando migration aplicada: version=%s", version)

    conn.execute(
        """
        INSERT INTO schema_migrations(version, applied_at)
        VALUES (?, datetime('now'))
        """,
        (version,),
    )

    conn.commit()


# ---------------------------------------------------------
# Descoberta de migrations
# ---------------------------------------------------------

def discover_migrations():
    """
    Descobre migrations válidas no diretório.

    Apenas arquivos no formato:

        NNN_nome.py

    serão considerados migrations.

    Returns
    -------
    list[(int,str)]
    """

    log.debug("Descobrindo migrations em %s", MIGRATIONS_DIR)

    migrations = []

    for file in MIGRATIONS_DIR.glob("*.py"):

        if file.name in ("__init__.py", "runner.py"):
            continue

        prefix = file.stem.split("_")[0]

        # ignora arquivos inválidos
        if not prefix.isdigit():
            log.debug("Arquivo ignorado (prefixo inválido): %s", file.name)
            continue

        version = int(prefix)

        module_name = file.stem

        migrations.append((version, module_name))

    migrations.sort(key=lambda x: x[0])

    log.debug("Migrations descobertas: %s", migrations)

    validate_migrations(migrations)

    return migrations


def validate_migrations(migrations):
    """
    Valida integridade das migrations.

    Verifica:

    - versões duplicadas
    - gaps na sequência
    """

    versions = [v for v, _ in migrations]

    if len(versions) != len(set(versions)):

        log.error("Versões duplicadas detectadas nas migrations.")

        raise RuntimeError("Duplicate migration versions detected.")

    if not versions:
        log.debug("Nenhuma migration encontrada.")
        return

    expected = list(range(min(versions), max(versions) + 1))

    if versions != expected:

        log.error("Gap detectado na sequência de migrations: %s", versions)

        raise RuntimeError(
            f"Migration sequence gap detected: {versions}"
        )


# ---------------------------------------------------------
# Compatibilidade com bancos antigos
# ---------------------------------------------------------

def legacy_database_detected(conn):
    """
    Detecta bancos antigos sem controle de migrations.
    """

    log.debug("Verificando se banco é legado.")

    cursor = conn.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='ticks'
    """)

    detected = cursor.fetchone() is not None

    if detected:
        log.info("Banco legado detectado (tabela ticks presente).")

    return detected


def bootstrap_legacy(conn):
    """
    Inicializa migrations em banco legado.
    """

    if legacy_database_detected(conn):

        log.info("Inicializando controle de migrations para banco legado.")

        conn.execute("""
            INSERT OR IGNORE INTO schema_migrations(version, applied_at)
            VALUES (1, datetime('now'))
        """)

        conn.commit()


# ---------------------------------------------------------
# Runner principal
# ---------------------------------------------------------

def run_migrations(conn):
    """
    Executa migrations pendentes.

    Fluxo:

    1. Garante tabela `schema_migrations`
    2. Detecta bancos legados
    3. Descobre migrations
    4. Executa migrations pendentes
    """

    log.debug("Iniciando verificação de migrations.")

    ensure_migrations_table(conn)

    bootstrap_legacy(conn)

    current = get_current_version(conn)

    migrations = discover_migrations()

    pending = [m for m in migrations if m[0] > current]

    if not pending:

        log.debug("Nenhuma migration pendente.")

        return

    log.info("Executando %s migration(s) pendente(s).", len(pending))

    for version, module_name in pending:

        module_path = f"{PACKAGE}.{module_name}"

        log.info("Aplicando migration %s (%s)", version, module_name)

        module = importlib.import_module(module_path)

        if not hasattr(module, "upgrade"):

            log.error("Migration %s não define upgrade()", module_name)

            raise RuntimeError(
                f"Migration {module_name} does not define upgrade()"
            )

        try:

            module.upgrade(conn)

            mark_version(conn, version)

            log.info("Migration %s aplicada com sucesso.", version)

        except Exception:

            log.exception("Falha ao aplicar migration %s", version)

            raise

    log.info("Migrations concluídas com sucesso.")

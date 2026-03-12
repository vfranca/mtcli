"""
Migration Runner do mtcli.

Este módulo é responsável por:

1. Descobrir migrations disponíveis no diretório `mtcli/migrations`
2. Determinar a versão atual do schema no banco
3. Executar migrations pendentes em ordem
4. Registrar migrations aplicadas na tabela `schema_migrations`

As migrations devem seguir o padrão:

    NNN_nome_da_migration.py

Exemplo:

    001_initial_schema.py
    002_ticks_time_msc.py
    003_optimize_ticks_without_rowid.py

Cada migration deve expor uma função:

    def upgrade(conn)

que recebe uma conexão SQLite ativa.
"""

import importlib
from pathlib import Path


MIGRATIONS_DIR = Path(__file__).parent
PACKAGE = "mtcli.migrations"


def get_current_version(conn):
    """
    Retorna a versão atual do schema registrada no banco.

    A versão corresponde ao maior número presente na
    tabela `schema_migrations`.

    Parameters
    ----------
    conn : sqlite3.Connection
        Conexão ativa com o banco SQLite.

    Returns
    -------
    int
        Versão atual do schema. Retorna 0 se nenhuma migration
        tiver sido aplicada.
    """

    cursor = conn.execute(
        "SELECT MAX(version) FROM schema_migrations"
    )

    row = cursor.fetchone()

    return row[0] if row and row[0] else 0


def mark_version(conn, version):
    """
    Registra uma migration como aplicada.

    Insere um registro na tabela `schema_migrations`
    contendo a versão aplicada e o timestamp.

    Parameters
    ----------
    conn : sqlite3.Connection
        Conexão com o banco.
    version : int
        Número da migration aplicada.
    """

    conn.execute(
        """
        INSERT INTO schema_migrations(version, applied_at)
        VALUES (?, datetime('now'))
        """,
        (version,),
    )

    conn.commit()


def discover_migrations():
    """
    Descobre automaticamente as migrations disponíveis.

    A função varre o diretório `mtcli/migrations` e retorna
    todas as migrations encontradas ordenadas pela versão.

    Returns
    -------
    list[tuple[int, str]]
        Lista de tuplas contendo:

        (version, module_name)

        Exemplo:
        [
            (1, "001_initial_schema"),
            (2, "002_ticks_time_msc"),
            (3, "003_optimize_ticks_without_rowid")
        ]
    """

    migrations = []

    for file in MIGRATIONS_DIR.glob("*.py"):

        if file.name in ("__init__.py", "runner.py"):
            continue

        version = int(file.name.split("_")[0])

        module_name = file.stem

        migrations.append((version, module_name))

    migrations.sort(key=lambda x: x[0])

    return migrations


def legacy_database_detected(conn):
    """
    Detecta se o banco já possui schema anterior às migrations.

    Alguns usuários podem ter bancos antigos criados antes
    da introdução do sistema de migrations.

    Neste caso detectamos a presença da tabela `ticks`
    como indício de banco legado.

    Parameters
    ----------
    conn : sqlite3.Connection

    Returns
    -------
    bool
        True se um schema legado for detectado.
    """

    cursor = conn.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='ticks'
    """)

    return cursor.fetchone() is not None


def bootstrap_legacy(conn):
    """
    Inicializa o controle de migrations para bancos legados.

    Se um banco antigo já possui a tabela `ticks`, assumimos
    que a migration inicial (001) já foi aplicada manualmente.

    Nesse caso registramos a versão 1 na tabela
    `schema_migrations`.

    Isso evita que a migration inicial tente recriar
    tabelas existentes.
    """

    if legacy_database_detected(conn):

        conn.execute("""
            INSERT OR IGNORE INTO schema_migrations(version, applied_at)
            VALUES (1, datetime('now'))
        """)

        conn.commit()


def run_migrations(conn):
    """
    Executa todas as migrations pendentes.

    Fluxo de execução:

    1. Verifica se o banco é legado
    2. Determina versão atual do schema
    3. Descobre migrations disponíveis
    4. Executa migrations ainda não aplicadas
    5. Registra cada migration aplicada

    Parameters
    ----------
    conn : sqlite3.Connection
        Conexão ativa com o banco SQLite.
    """

    bootstrap_legacy(conn)

    current = get_current_version(conn)

    migrations = discover_migrations()

    for version, module_name in migrations:

        if version <= current:
            continue

        module_path = f"{PACKAGE}.{module_name}"

        module = importlib.import_module(module_path)

        print(f"Applying migration {version}: {module_name}")

        module.upgrade(conn)

        mark_version(conn, version)

    print("Migrations concluídas.")

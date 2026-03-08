import importlib
from pathlib import Path


MIGRATIONS_DIR = Path(__file__).parent
PACKAGE = "mtcli.migrations"


def get_current_version(conn):

    cursor = conn.execute(
        "SELECT MAX(version) FROM schema_migrations"
    )

    row = cursor.fetchone()

    return row[0] if row and row[0] else 0


def mark_version(conn, version):

    conn.execute(
        """
        INSERT INTO schema_migrations(version, applied_at)
        VALUES (?, datetime('now'))
        """,
        (version,),
    )

    conn.commit()


def discover_migrations():

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

    cursor = conn.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='ticks'
    """)

    return cursor.fetchone() is not None


def bootstrap_legacy(conn):

    """
    Marca migration 1 como aplicada se banco já tinha schema.
    """

    if legacy_database_detected(conn):

        conn.execute("""
            INSERT OR IGNORE INTO schema_migrations(version, applied_at)
            VALUES (1, datetime('now'))
        """)

        conn.commit()


def run_migrations(conn):

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

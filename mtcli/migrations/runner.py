import importlib
from pathlib import Path


MIGRATIONS = [
    "mtcli.migrations.001_initial_schema",
    "mtcli.migrations.002_ticks_time_msc",
]


def get_current_version(conn):

    cursor = conn.execute("""
        SELECT MAX(version) FROM schema_migrations
    """)

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

    for i, module_path in enumerate(MIGRATIONS, start=1):

        if i <= current:
            continue

        module = importlib.import_module(module_path)

        print(f"Applying migration {i}")

        module.upgrade(conn)

        mark_version(conn, i)

    print("Migrations concluídas.")

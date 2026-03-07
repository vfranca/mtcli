import importlib

MIGRATIONS = [
    "mtcli.migrations.001_initial_schema",
    "mtcli.migrations.002_ticks_time_msc",
]


def run_migrations(conn):

    conn.execute("""
        CREATE TABLE IF NOT EXISTS schema_migrations (
            version INTEGER PRIMARY KEY,
            applied_at TEXT
        )
    """)

    cur = conn.cursor()

    cur.execute("SELECT version FROM schema_migrations")

    applied = {row[0] for row in cur.fetchall()}

    for i, module_path in enumerate(MIGRATIONS, start=1):

        if i in applied:
            continue

        module = importlib.import_module(module_path)

        print(f"Applying migration {i}")

        module.upgrade(conn)

        conn.execute(
            "INSERT INTO schema_migrations VALUES (?, datetime('now'))",
            (i,)
        )

        conn.commit()

"""
Migration 004

Reconstrói a tabela `ticks` utilizando `time_msc` como parte
da chave primária.

Motivação:

- `time` possui resolução em segundos
- `time_msc` possui resolução em milissegundos
- múltiplos ticks podem ocorrer dentro do mesmo segundo

Nova chave primária:

    PRIMARY KEY(symbol, time_msc)
"""


def upgrade(conn):
    """
    Reconstrói a tabela `ticks` alterando a chave primária
    para `(symbol, time_msc)`.
    """

    cursor = conn.execute("""
        SELECT sql
        FROM sqlite_master
        WHERE type='table'
        AND name='ticks'
    """)

    row = cursor.fetchone()

    if not row:
        return

    if "PRIMARY KEY(symbol, time_msc)" in row[0]:
        return

    print("Rebuilding ticks table with PK(symbol,time_msc)...")

    conn.execute("PRAGMA foreign_keys=OFF")

    conn.execute("""
    CREATE TABLE ticks_new(
        symbol TEXT NOT NULL,
        time INTEGER NOT NULL,
        time_msc INTEGER NOT NULL,
        bid REAL,
        ask REAL,
        last REAL,
        volume REAL,
        flags INTEGER,
        PRIMARY KEY(symbol, time_msc)
    ) WITHOUT ROWID
    """)

    conn.execute("""
    INSERT INTO ticks_new
    SELECT
        symbol,
        time,
        COALESCE(time_msc,time),
        bid,
        ask,
        last,
        volume,
        flags
    FROM ticks
    """)

    conn.execute("DROP TABLE ticks")

    conn.execute("ALTER TABLE ticks_new RENAME TO ticks")

    conn.commit()

    print("ticks table rebuilt with PK(symbol,time_msc)")

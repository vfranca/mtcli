def upgrade(conn):

    conn.execute("""
    CREATE TABLE IF NOT EXISTS ticks(
        symbol TEXT NOT NULL,
        time INTEGER NOT NULL,
        bid REAL,
        ask REAL,
        last REAL,
        volume REAL,
        flags INTEGER,
        PRIMARY KEY(symbol, time)
    )
    """)

    conn.execute("""
    CREATE INDEX IF NOT EXISTS idx_ticks_symbol_time
    ON ticks(symbol, time)
    """)

    conn.commit()

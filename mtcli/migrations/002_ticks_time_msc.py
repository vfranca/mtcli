def upgrade(conn):

    conn.execute("""
        CREATE TABLE ticks_new (
            symbol TEXT NOT NULL,
            time INTEGER NOT NULL,
            time_msc INTEGER NOT NULL,
            bid REAL,
            ask REAL,
            last REAL,
            volume REAL,
            flags INTEGER,
            PRIMARY KEY(symbol, time_msc)
        )
    """)

    conn.execute("""
        INSERT INTO ticks_new
        SELECT
            symbol,
            time,
            time * 1000,
            bid,
            ask,
            last,
            volume,
            flags
        FROM ticks
    """)

    conn.execute("DROP TABLE ticks")

    conn.execute("ALTER TABLE ticks_new RENAME TO ticks")

    conn.execute("""
        CREATE INDEX idx_ticks_symbol_time_msc
        ON ticks(symbol, time_msc)
    """)

    conn.commit()

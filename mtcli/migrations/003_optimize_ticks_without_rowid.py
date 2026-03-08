def upgrade(conn):

    cursor = conn.execute("""
        SELECT sql
        FROM sqlite_master
        WHERE type='table'
        AND name='ticks'
    """)

    row = cursor.fetchone()

    if not row:
        return

    if "WITHOUT ROWID" in row[0]:
        return

    print("Optimizing ticks table (WITHOUT ROWID)...")

    conn.execute("PRAGMA foreign_keys=OFF")

    conn.execute("""
    CREATE TABLE ticks_new(
        symbol TEXT NOT NULL,
        time INTEGER NOT NULL,
        time_msc INTEGER,
        bid REAL,
        ask REAL,
        last REAL,
        volume REAL,
        flags INTEGER,
        PRIMARY KEY(symbol, time)
    ) WITHOUT ROWID
    """)

    conn.execute("""
    INSERT INTO ticks_new
    SELECT
        symbol,
        time,
        time_msc,
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

    conn.execute("PRAGMA foreign_keys=ON")

    conn.commit()

    print("ticks table optimized.")

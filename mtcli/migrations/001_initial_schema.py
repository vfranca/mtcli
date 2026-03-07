def upgrade(conn):

    conn.execute("""
        CREATE TABLE ticks (
            symbol TEXT NOT NULL,
            time INTEGER NOT NULL,
            bid REAL,
            ask REAL,
            last REAL,
            volume REAL,
            flags INTEGER,
            PRIMARY KEY(symbol, time)
        );
    """)

    conn.commit()

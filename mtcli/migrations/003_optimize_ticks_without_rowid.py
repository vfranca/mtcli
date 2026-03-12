"""
Migration 003

Otimiza a tabela `ticks` convertendo-a para `WITHOUT ROWID`.

Tabelas SQLite com chave primária composta podem ter melhor
performance e menor uso de disco utilizando `WITHOUT ROWID`.

Para aplicar esta otimização é necessário reconstruir a tabela.
"""


def upgrade(conn):
    """
    Reconstrói a tabela `ticks` utilizando `WITHOUT ROWID`.

    Processo executado:

    1. Cria nova tabela otimizada
    2. Copia os dados da tabela antiga
    3. Remove tabela antiga
    4. Renomeia nova tabela
    5. Recria índices necessários
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

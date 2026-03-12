"""
Migration 005

Aplica compressão de preços nos ticks.

Preços e volume passam a ser armazenados como inteiros
para reduzir uso de espaço em disco.

Transformações aplicadas:

    bid   -> INTEGER (bid * 100)
    ask   -> INTEGER (ask * 100)
    last  -> INTEGER (last * 100)
    volume -> INTEGER

A tabela precisa ser reconstruída para alterar os tipos
das colunas.
"""


def upgrade(conn):
    """
    Reconstrói a tabela `ticks` aplicando compressão
    de preços e volumes.

    Isso reduz significativamente o tamanho do banco
    e melhora performance de leitura.
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

    if "bid INTEGER" in row[0]:
        return

    print("Applying tick compression...")

    conn.execute("PRAGMA foreign_keys=OFF")

    conn.execute("""
    CREATE TABLE ticks_new(
        symbol TEXT NOT NULL,
        time_msc INTEGER NOT NULL,
        bid INTEGER,
        ask INTEGER,
        last INTEGER,
        volume INTEGER,
        flags INTEGER,
        PRIMARY KEY(symbol,time_msc)
    ) WITHOUT ROWID
    """)

    conn.execute("""
    INSERT INTO ticks_new
    SELECT
        symbol,
        time_msc,
        CAST(bid*100 AS INTEGER),
        CAST(ask*100 AS INTEGER),
        CAST(last*100 AS INTEGER),
        CAST(volume AS INTEGER),
        flags
    FROM ticks
    """)

    conn.execute("DROP TABLE ticks")

    conn.execute("ALTER TABLE ticks_new RENAME TO ticks")

    conn.execute("""
    CREATE INDEX idx_ticks_symbol_time_msc
    ON ticks(symbol,time_msc)
    """)

    conn.commit()

    print("Tick compression applied.")

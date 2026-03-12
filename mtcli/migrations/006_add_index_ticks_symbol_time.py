"""
Migration 006

Cria índice para acelerar consultas por símbolo e tempo
utilizando a coluna `time_msc`.

Este índice é importante para consultas comuns como:

    SELECT * FROM ticks
    WHERE symbol = ?
    ORDER BY time_msc
"""

SQL = """
CREATE INDEX IF NOT EXISTS idx_ticks_symbol_time
ON ticks(symbol, time_msc);
"""


def upgrade(conn):
    """
    Executa a criação do índice `idx_ticks_symbol_time`.

    A operação é idempotente graças ao uso de
    `CREATE INDEX IF NOT EXISTS`.
    """

    cursor = conn.cursor()

    cursor.execute(SQL)

    conn.commit()

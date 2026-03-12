"""
Migration 002

Adiciona a coluna `time_msc` à tabela `ticks`.

A API do MetaTrader fornece timestamps com resolução em
milissegundos (`time_msc`). Esta migration adiciona suporte
a esse campo sem quebrar compatibilidade com bancos antigos.
"""


def column_exists(conn, table, column):
    """
    Verifica se uma coluna existe em uma tabela SQLite.

    Parameters
    ----------
    conn : sqlite3.Connection
        Conexão com o banco de dados.
    table : str
        Nome da tabela.
    column : str
        Nome da coluna.

    Returns
    -------
    bool
        True se a coluna existir.
    """

    cursor = conn.execute(f"PRAGMA table_info({table})")

    for row in cursor.fetchall():
        if row[1] == column:
            return True

    return False


def upgrade(conn):
    """
    Adiciona a coluna `time_msc` à tabela `ticks`
    caso ela ainda não exista.
    """

    if not column_exists(conn, "ticks", "time_msc"):

        conn.execute("""
        ALTER TABLE ticks
        ADD COLUMN time_msc INTEGER
        """)

    conn.commit()

"""
Migration 008

Corrige problemas da migration 007.

Problemas corrigidos:

1. SELECT DISTINCT * não removia duplicados corretamente
2. índice redundante (symbol,time_msc)
3. possível permanência de duplicados

Estratégia segura:

1. criar nova tabela
2. inserir dados usando INSERT OR IGNORE
3. criar índice UNIQUE
4. substituir tabela antiga
"""

from sqlite3 import Connection


def upgrade(conn: Connection):

    cursor = conn.cursor()

    # ---------------------------------------------------------
    # 1 criar nova tabela
    # ---------------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE ticks_new AS
        SELECT *
        FROM ticks
        WHERE 0
        """
    )

    # ---------------------------------------------------------
    # 2 copiar dados removendo duplicados
    # ---------------------------------------------------------

    cursor.execute(
        """
        CREATE UNIQUE INDEX idx_ticks_unique_temp
        ON ticks_new(symbol, time_msc)
        """
    )

    cursor.execute(
        """
        INSERT OR IGNORE INTO ticks_new
        SELECT *
        FROM ticks
        ORDER BY time_msc
        """
    )

    # ---------------------------------------------------------
    # 3 remover tabela antiga
    # ---------------------------------------------------------

    cursor.execute("DROP TABLE ticks")

    # ---------------------------------------------------------
    # 4 renomear tabela
    # ---------------------------------------------------------

    cursor.execute(
        "ALTER TABLE ticks_new RENAME TO ticks"
    )

    # ---------------------------------------------------------
    # 5 recriar índice UNIQUE definitivo
    # ---------------------------------------------------------

    cursor.execute(
        """
        CREATE UNIQUE INDEX idx_ticks_unique
        ON ticks(symbol, time_msc)
        """
    )

    conn.commit()


def downgrade(conn: Connection):

    cursor = conn.cursor()

    cursor.execute(
        """
        DROP INDEX IF EXISTS idx_ticks_unique
        """
    )

    conn.commit()

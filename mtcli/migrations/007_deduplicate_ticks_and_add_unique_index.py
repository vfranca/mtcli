"""
Migration 007

Objetivo
--------

1. Remover registros duplicados da tabela `ticks`
2. Criar índice UNIQUE para evitar duplicação futura

Critério de unicidade adotado:

    (symbol, time_msc)

Estratégia
----------

1. Criar tabela temporária com SELECT DISTINCT
2. Copiar dados únicos
3. Substituir tabela original
4. Criar índice UNIQUE

Essa estratégia é muito mais rápida do que DELETE em tabelas grandes.
"""

from sqlite3 import Connection


def upgrade(conn: Connection) -> None:
    cursor = conn.cursor()

    # ---------------------------------------------------------
    # 1 - criar nova tabela sem duplicados
    # ---------------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ticks_new AS
        SELECT DISTINCT *
        FROM ticks
        """
    )

    # ---------------------------------------------------------
    # 2 - remover tabela antiga
    # ---------------------------------------------------------

    cursor.execute("DROP TABLE ticks")

    # ---------------------------------------------------------
    # 3 - renomear tabela nova
    # ---------------------------------------------------------

    cursor.execute("ALTER TABLE ticks_new RENAME TO ticks")

    # ---------------------------------------------------------
    # 4 - recriar índice de performance existente
    # ---------------------------------------------------------

    cursor.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_ticks_symbol_time
        ON ticks(symbol, time_msc)
        """
    )

    # ---------------------------------------------------------
    # 5 - criar índice UNIQUE
    # ---------------------------------------------------------

    cursor.execute(
        """
        CREATE UNIQUE INDEX IF NOT EXISTS idx_ticks_unique
        ON ticks(symbol, time_msc)
        """
    )

    conn.commit()


def downgrade(conn: Connection) -> None:
    cursor = conn.cursor()

    # Remove índice UNIQUE caso exista rollback

    cursor.execute(
        """
        DROP INDEX IF EXISTS idx_ticks_unique
        """
    )

    conn.commit()

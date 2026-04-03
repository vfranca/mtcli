"""
Migration 009

Objetivo
--------

Remover todos os ticks que não são trade ticks.

Critério de trade tick:

    flags & 1 != 0

Estratégia:

1. Criar tabela temporária com apenas trade ticks.
2. Substituir tabela original.
3. Recriar índices existentes.
"""

from sqlite3 import Connection


def upgrade(conn: Connection) -> None:
    cursor = conn.cursor()

    # ---------------------------------------------------------
    # 1 - criar tabela temporária apenas com trade ticks
    # ---------------------------------------------------------

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ticks_trade_only AS
        SELECT *
        FROM ticks
        WHERE (flags & 1) != 0
        """
    )

    # ---------------------------------------------------------
    # 2 - remover tabela antiga
    # ---------------------------------------------------------

    cursor.execute("DROP TABLE ticks")

    # ---------------------------------------------------------
    # 3 - renomear tabela nova
    # ---------------------------------------------------------

    cursor.execute("ALTER TABLE ticks_trade_only RENAME TO ticks")

    # ---------------------------------------------------------
    # 4 - recriar índices existentes
    # ---------------------------------------------------------

    cursor.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_ticks_symbol_time
        ON ticks(symbol, time_msc)
        """
    )

    cursor.execute(
        """
        CREATE UNIQUE INDEX IF NOT EXISTS idx_ticks_unique
        ON ticks(symbol, time_msc)
        """
    )

    cursor.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_ticks_time
        ON ticks(time_msc)
        """
    )

    conn.commit()


def downgrade(conn: Connection) -> None:
    """
    Não é possível restaurar os ticks removidos
    em caso de downgrade.
    """
    pass

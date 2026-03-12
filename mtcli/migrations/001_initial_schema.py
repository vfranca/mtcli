"""
Migration 001

Cria o schema inicial do banco de dados do mtcli.

Esta migration cria a tabela principal `ticks`, responsável por
armazenar os ticks de mercado capturados do MetaTrader.

Estrutura inicial:

- symbol : símbolo do ativo
- time   : timestamp em segundos
- bid    : preço bid
- ask    : preço ask
- last   : último preço negociado
- volume : volume do tick
- flags  : flags fornecidas pela API MT5

Também cria o índice `idx_ticks_symbol_time` para acelerar
consultas por símbolo e tempo.
"""


def upgrade(conn):
    """
    Executa a migration inicial criando a tabela `ticks`
    e o índice principal utilizado nas consultas.

    A operação é idempotente graças ao uso de
    `CREATE TABLE IF NOT EXISTS`.
    """

    conn.execute("""
    CREATE TABLE IF NOT EXISTS ticks(
        symbol TEXT NOT NULL,
        time INTEGER NOT NULL,
        bid REAL,
        ask REAL,
        last REAL,
        volume REAL,
        flags INTEGER,
        PRIMARY KEY(symbol, time)
    )
    """)

    conn.execute("""
    CREATE INDEX IF NOT EXISTS idx_ticks_symbol_time
    ON ticks(symbol, time)
    """)

    conn.commit()

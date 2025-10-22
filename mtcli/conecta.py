"""
Gerencia a conexão direta com o terminal MetaTrader 5.
Usado internamente pelo contexto mt5_conexao().
"""

import MetaTrader5 as mt5

from mtcli.logger import setup_logger

log = setup_logger()


def conectar() -> bool:
    """
    Inicializa a conexão com o MetaTrader 5.

    Retorna:
        bool: True se conectado com sucesso, False caso contrário.

    Levanta:
        ConnectionError: se a inicialização do MT5 falhar.
    """
    log.debug("Tentando inicializar conexao com MetaTrader 5...")

    if not mt5.initialize():
        erro = mt5.last_error()
        log.error(f"Erro ao conectar ao MetaTrader 5: {erro}")
        raise ConnectionError(f"Falha ao conectar ao MetaTrader 5: {erro}")

    log.info("Conexao com MetaTrader 5 estabelecida com sucesso.")
    return True


def shutdown():
    """
    Encerra a conexão com o MetaTrader 5 de forma segura.
    """
    try:
        mt5.shutdown()
        log.debug("Conexao com MetaTrader 5 encerrada.")
    except Exception as e:
        log.error(f"Erro ao encerrar conexao com MetaTrader 5: {e}")

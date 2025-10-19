"""
Gerencia o ciclo de conexão com o MetaTrader 5.
Fornece o contexto 'mt5_conexao' para uso seguro em blocos with.
"""

from contextlib import contextmanager
from mtcli.logger import setup_logger
from mtcli.conecta import conectar, shutdown

log = setup_logger()


@contextmanager
def mt5_conexao():
    """
    Context manager para conexão com o MetaTrader 5.
    - Chama `conectar()` ao entrar no contexto.
    - Chama `shutdown()` ao sair.
    - Loga falhas e garante fechamento seguro.
    """
    try:
        log.debug("Inicializando conexao com MetaTrader 5...")
        conectar()
        yield
    except Exception as e:
        log.error(f"Erro ao conectar ao MetaTrader 5: {e}")
        raise
    finally:
        try:
            shutdown()
            log.debug("Conexao com MetaTrader 5 encerrada.")
        except Exception as e:
            log.error(f"Erro ao encerrar conexao MT5: {e}")

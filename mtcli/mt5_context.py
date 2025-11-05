"""
Gerencia o ciclo de conexão com o MetaTrader 5.
Fornece o contexto 'mt5_conexao' para uso seguro em blocos with.
"""

from contextlib import contextmanager
import MetaTrader5 as mt5
from mtcli.logger import setup_logger

log = setup_logger()


@contextmanager
def mt5_conexao():
    """
    Context manager para conexão direta com o MetaTrader 5.
    - Chama `mt5.initialize()` ao entrar no contexto.
    - Chama `mt5.shutdown()` ao sair.
    - Loga falhas e garante fechamento seguro.
    """
    try:
        log.info("Inicializando conexão com MetaTrader 5 via API oficial...")
        if not mt5.initialize():
            error = mt5.last_error()
            log.error(f"Falha ao inicializar MetaTrader 5: {error}")
            raise RuntimeError(f"Erro ao conectar ao MT5: {error}")
        yield
    except Exception as e:
        log.error(f"Erro durante o uso da conexão MT5: {e}")
        raise
    finally:
        try:
            mt5.shutdown()
            log.info("Conexão com MetaTrader 5 encerrada com sucesso.")
        except Exception as e:
            log.error(f"Erro ao encerrar conexão MT5: {e}")

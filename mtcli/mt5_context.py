"""
Gerencia o ciclo de conexão com o MetaTrader 5.
Fornece o contexto 'mt5_conexao' para uso seguro em blocos with.
"""

from contextlib import contextmanager

import MetaTrader5 as mt5

from mtcli.logger import setup_logger

log = setup_logger()


@contextmanager
def mt5_conexao(
    login: int | None = None, password: str | None = None, server: str | None = None
):
    """
    Context manager para conexão direta com o MetaTrader 5.

    Parâmetros opcionais:
        - login (int): número da conta MT5.
        - password (str): senha da conta.
        - server (str): nome do servidor.

    Uso:
        >>> with mt5_conexao(login=123456, password="senha", server="ClearInvestimentos-Real"):
        ...     info = mt5.account_info()
        ...     print(info)

    Comportamento:
        - Se as credenciais forem fornecidas, tenta autenticar a conta.
        - Caso contrário, conecta-se à sessão já ativa do terminal MT5.
        - Garante encerramento seguro da conexão.
    """
    try:
        log.info("Inicializando conexão com MetaTrader 5 via API oficial...")

        if login and password and server:
            if not mt5.initialize(login=login, password=password, server=server):
                error = mt5.last_error()
                log.error(f"Falha ao conectar ao MetaTrader 5: {error}")
                raise RuntimeError(f"Erro ao conectar ao MT5: {error}")
            else:
                log.info(f"Conectado à conta MT5 {login} ({server}).")
        else:
            if not mt5.initialize():
                error = mt5.last_error()
                log.error(f"Falha ao inicializar MetaTrader 5: {error}")
                raise RuntimeError(f"Erro ao conectar ao MT5: {error}")
            else:
                log.info("Conectado à sessão ativa do MetaTrader 5.")

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

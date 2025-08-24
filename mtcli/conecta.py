"""Módulo de conexão com o MetaTrader 5."""

import MetaTrader5 as mt5
from mtcli.logger import setup_logger

logger = setup_logger()


def conectar():
    if not mt5.initialize():
        click.echo(f"❌ Erro ao conectar ao MT5: {mt5.last_error()}")
        logger.error(f"Erro ao conectar ao MT5: {mt5.last_error()}")
        exit()
    return True


def shutdown():
    mt5.shutdown()

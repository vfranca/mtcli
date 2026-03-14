import click
import datetime
import MetaTrader5 as mt5

from mtcli.marketdata.tick_repository import TickRepository
from mtcli.logger import setup_logger

log = setup_logger(__name__)


@click.command()
@click.argument("symbol")
@click.option("--days", default=5, help="Número de dias de histórico")
def backfill(symbol, days):
    """
    Carrega ticks históricos do MT5 para o banco.
    """

    log.info("Backfill iniciado para %s (%s dias)", symbol, days)

    if not mt5.initialize():
        log.error("Falha ao inicializar MT5")
        return

    mt5.symbol_select(symbol, True)

    to_date = datetime.datetime.utcnow()
    from_date = to_date - datetime.timedelta(days=days)

    ticks = mt5.copy_ticks_range(
        symbol,
        from_date,
        to_date,
        mt5.COPY_TICKS_ALL
    )

    if ticks is None or len(ticks) == 0:
        log.warning("Nenhum tick retornado")
        return

    repo = TickRepository()

    repo.insert_ticks(symbol, ticks)

    log.info("Backfill concluído: %s ticks", len(ticks))

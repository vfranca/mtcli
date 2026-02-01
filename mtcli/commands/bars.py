import click

from mtcli.controllers.bars_controller import BarsController
from mtcli.data.mt5 import MT5DataSource


@click.command()
@click.argument("symbol")
@click.option("--period", default="m1", help="Timeframe (ex: m1, m5, h1, d1)")
@click.option("--count", default=20, help="Quantidade de barras")
@click.option("--view", default="min", help="View: min, full, range, volume, rate")
@click.option("--date", default=None, help="Filtrar por data (YYYY-MM-DD)")
@click.option("--numerator", is_flag=True, help="Numerar barras")
@click.option("--show-date", is_flag=True, help="Exibir data ou hora")
@click.option("--volume", default=None, help="Modo de volume")
def bars(symbol, period, count, view, date, numerator, show_date, volume):
    """
    Exibe barras de preço no terminal.
    """
    controller = BarsController(MT5DataSource())

    lines = controller.execute(
        symbol=symbol,
        period=period,
        count=count,
        date=date,
        view=view,
        numerator=numerator,
        show_date=show_date,
        volume=volume,
    )

    for line in lines:
        click.echo(line)

import click

from mtcli.controllers.bars_controller import BarsController
from mtcli.conf import (
    DATA_SOURCE_NAME,
    SYMBOL,
    TIMEFRAME,
    BARS,
    VIEW,
    VOLUME_TYPE,
)
from mtcli.data.factory import create_data_source


@click.command()
@click.option("--symbol", "-s", default=SYMBOL, show_default=True, help="Codigo do ativo")
@click.option("--timeframe", "-t", "period", default=TIMEFRAME, show_default=True, help="Timeframe do grafico")
@click.option("--bars", "-b", "count", default=BARS, show_default=True, help="Quantidade de barras")
@click.option("--view", "-v", default=VIEW, show_default=True, help="Formato de visualizacao")
@click.option("--date", "-d", default=None, show_default=True, help="Filtrar pregao por data (YYYY-MM-DD)")
@click.option("--numerator", "-n", is_flag=True, show_default=True, help="Numerar barras")
@click.option("--show-date", "-sd", is_flag=True, show_default=True, help="Exibir data ou hora")
@click.option("--volume-type", "-vt", "volume", default=VOLUME_TYPE, show_default=True, help="Tipo de volume (real ou tick)")
@click.option("--data-source", "-ds", "source", default=None, show_default=True, help="Fonte de dados (mt5 ou csv)")
def bars(symbol, period, count, view, date, numerator, show_date, volume, source):
    """
    Exibe barras de preço no terminal.
    """

    source_name = source or DATA_SOURCE_NAME
    data_source = create_data_source(source_name)

    controller = BarsController(data_source)

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

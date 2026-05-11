"""
Comando CLI `bars`.

Responsável por:
- receber parâmetros via terminal (Click)
- instanciar a fonte de dados
- delegar execução ao BarsController
- imprimir saída no terminal

Este comando é a camada de entrada (CLI) no padrão MVC do mtcli.
"""

import click

from ..controllers.bars_controller import BarsController
from ..conf import (
    DATA_SOURCE_NAME,
    SYMBOL,
    TIMEFRAME,
    MAX_BARS,
    VIEW,
    VOLUME_TYPE,
)
from ..data.factory import create_data_source


@click.command()
@click.option("--symbol", "-s", default=SYMBOL, show_default=True, help="Código do ativo (ex: WINM26)")
@click.option("--timeframe", "-t", "period", default=TIMEFRAME, show_default=True, help="Timeframe (ex: M1, M5, D1)")
@click.option("--max-bars", "-mb", "count", default=MAX_BARS, show_default=True, help="Quantidade de barras")
@click.option("--view", "-v", default=VIEW, show_default=True, help="Formato da view (hl_view, full_view, etc)")
@click.option("--date", "-d", default=None, show_default=True, help="Filtrar pregão (YYYY-MM-DD)")
@click.option("--numerator", "-n", is_flag=True, show_default=True, help="Numerar barras")
@click.option("--show-date", "-sd", is_flag=True, show_default=True, help="Exibir data/hora")
@click.option("--volume-type", "-vt", "volume", default=VOLUME_TYPE, show_default=True, help="Tipo de volume (tick/real)")
@click.option("--data-source", "-ds", "source", default=None, show_default=True, help="Fonte de dados (mt5/csv)")
def bars(symbol, period, count, view, date, numerator, show_date, volume, source):
    """
    Executa o comando `bars`.

    Fluxo:
    1. Resolve fonte de dados
    2. Executa controller
    3. Renderiza saída linha a linha

    Args:
        symbol (str): Ativo
        period (str): Timeframe
        count (int): Quantidade de barras
        view (str): Nome da view
        date (str | None): Filtro de pregão
        numerator (bool): Numerar barras
        show_date (bool): Mostrar timestamp
        volume (str | None): Tipo de volume
        source (str | None): Fonte de dados
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

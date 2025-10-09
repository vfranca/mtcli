"""Calcula o range médio das barras."""

import click

from mtcli.models.rates_model import RatesModel
from . import conf
from .models.average_range_model import AverageRangeModel


@click.command(
    "rm", help="Calcula o range médio de preços do ativo em um determinado período."
)
@click.argument("symbol")
@click.option(
    "--period",
    "-p",
    type=click.Choice(conf.timeframes, case_sensitive=False),
    default="D1",
    help="Tempo grafico, default D1.",
)
@click.option(
    "--periodos", "-pe", default=14, help="Quantidade de periodos; default 14."
)
def rm(symbol, period, periodos):
    """Calcula o range medio do ativo symbol."""
    rates = RatesModel(symbol, period).get_data()
    rm = AverageRangeModel(rates, periodos).average()
    click.echo(rm)


if __name__ == "__main__":
    rm()

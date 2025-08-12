"""Calcula o range médio das barras."""

import click

from mtcli.models import model_rates

from . import conf
from .models import model_average_range


@click.command()
@click.argument("symbol")
@click.option(
    "--period",
    "-p",
    type=click.Choice(conf.timeframes, case_sensitive=False),
    default="D1",
    help="Tempo grafico, default D1.",
)
@click.option("--periodos", "-pe", default=14, help="Quantidade de periodos; default 14.")
def rm(symbol, period, periodos):
    """Calcula o range medio do ativo symbol."""
    rates = model_rates.RatesModel(symbol, period).lista
    rm = model_average_range.AverageRangeModel(rates, periodos)
    rm = rm.average()
    click.echo(rm)


if __name__ == "__main__":
    rm()

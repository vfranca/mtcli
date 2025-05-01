"""Calcula o range médio das barras."""

import click

from mtcli import conf
from mtcli.models import model_average_range, model_rates


@click.command()
@click.argument("symbol")
@click.option(
    "--period",
    "-p",
    type=click.Choice(conf.timeframes, case_sensitive=False),
    default="D1",
    help="Tempo grafico, default D1.",
)
@click.option("--count", "-c", default=10, help="Quantidade de barras, default 10.")
def rm(symbol, period, count):
    """Calcula o range medio das barras."""
    rates = model_rates.RatesModel(symbol, period)
    rates = rates.lista
    rm = model_average_range.AverageRangeModel(rates, count)
    rm = rm.average()
    click.echo(rm)


if __name__ == "__main__":
    rm()

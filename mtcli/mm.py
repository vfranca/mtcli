"""Calcula a média móvel simples."""

import click

from mtcli import conf
from mtcli.models import model_moving_average, model_rates


@click.command()
@click.argument("symbol")
@click.option(
    "--period",
    "-p",
    type=click.Choice(conf.timeframes, case_sensitive=False),
    default="D1",
    help="Tempo grafico, default D1.",
)
@click.option("--count", "-c", default=20, help="Quantidade de barras, default 20.")
def mm(symbol, period, count):
    """Calcula a media movel simples."""
    rates = model_rates.RatesModel(symbol, period)
    rates = rates.lista
    ma = model_moving_average.MovingAverageModel(rates, count)
    ma = ma.average()
    click.echo(ma)


if __name__ == "__main__":
    mm()

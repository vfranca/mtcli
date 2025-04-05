"""
Calcula o tamanho médio das barras
"""

import click
from mtcli.models import model_rates
from mtcli.models import model_ranges
from mtcli import conf


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
    """Calcula o tamanho medio das barras."""
    rates = model_rates.RatesModel(symbol, period)
    rates = rates.lista
    ranges = model_ranges.RangesModel(rates)
    ranges = ranges.lista
    ranges = ranges[-count:]
    rm = round(sum(ranges) / len(ranges), conf.digitos)
    click.echo(rm)


if __name__ == "__main__":
    rm()

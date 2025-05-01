"""Calcula o volume médio das barras."""

import click

from mtcli import conf
from mtcli.models import model_average_volume, model_rates


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
@click.option(
    "--type",
    "-t",
    type=click.Choice(["tick", "real"], case_sensitive=False),
    default="tick",
    help="Tipo de volume, default tick.",
)
def vm(symbol, period, count, type):
    """Calcula o volume medio das barras."""
    rates = model_rates.RatesModel(symbol, period)
    rates = rates.lista
    vm = model_average_volume.AverageVolumeModel(rates, count, type)
    vm = vm.average()
    click.echo(vm)


if __name__ == "__main__":
    vm()

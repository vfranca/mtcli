"""Calcula o volume médio das barras."""

import click

from mtcli import conf
from mtcli.models import model_volume_medio, model_rates


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
def vm(symbol, period, count):
    """Calcula o volume medio das barras."""
    rates = model_rates.RatesModel(symbol, period)
    rates = rates.lista
    vm = model_volume_medio.VolumeMedioModel(rates, count)
    vm = vm.media()
    click.echo(vm)


if __name__ == "__main__":
    vm()

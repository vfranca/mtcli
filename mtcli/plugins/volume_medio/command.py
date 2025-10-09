"""Calcula o volume médio das barras."""

import click

from mtcli.models.rates_model import RatesModel

from . import conf
from .models import model_average_volume


@click.command(
    "vm",
    help="Calcula o volume médio (em ticks ou financeiro) do ativo em determinado período.",
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
    "--periodos", "-pe", default=14, help="Quantidade de períodos da média, default 14."
)
@click.option(
    "--tipo",
    "-t",
    type=click.Choice(["tick", "real"], case_sensitive=False),
    default="tick",
    help="Tipo de volume tick ou real, default tick.",
)
def vm(symbol, period, periodos, tipo):
    """Calcula o volume médio (tick ou real) do ativo symbol."""
    rates = RatesModel(symbol, period).get_data()
    vm = model_average_volume.AverageVolumeModel(rates, periodos, tipo)
    vm = vm.average()
    click.echo(vm)


if __name__ == "__main__":
    vm()

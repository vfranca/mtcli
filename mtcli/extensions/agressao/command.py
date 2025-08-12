"""Exibe o saldo agressor."""

import click

from mtcli.models import model_bars, model_rates

from . import conf
from .models import model_agressao
from .views import view_agressao


@click.command()
@click.argument("symbol")
@click.option(
    "--period",
    "-p",
    type=click.Choice(conf.timeframes, case_sensitive=False),
    default="d1",
    help="Tempo grafico, default D1.",
)
@click.option(
    "--count", "-c", type=int, default=20, help="Quantidade de barras, default 20."
)
@click.option(
    "--volume",
    "-vo",
    type=click.Choice(["tick", "real"], case_sensitive=False),
    default="tick",
    help="Tipo de volume, default tick.",
)
def sa(symbol, period, count, volume):
    """Exibe o saldo da agressão."""
    period = period.lower()
    rates = model_rates.RatesModel(symbol, period)
    rates = rates.lista
    bars = model_bars.BarsModel(rates)
    bars = bars.lista
    agressao = model_agressao.AgressaoModel(bars, volume, count)
    saldo_agressao = agressao.get_saldo()
    view = view_agressao.AgressaoView(saldo_agressao)
    click.echo(view.view())


if __name__ == "__main__":
    sa()

"""
Exibe a média móvel do indicador MA_TXT
"""

import click
from mtcli.models import model_rates_ma
from mtcli.models import model_mas
from mtcli.views import view_ma
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
@click.option(
    "--count", "-c", type=int, default=20, help="Quantidade de barras, default 20."
)
def ma(symbol, period, count):
    """Exibe as medias moveis do indicador MA_TXT."""
    rates = model_rates_ma.RatesMaModel(symbol, period, count)
    rates = rates.lista()
    mas = model_mas.MasModel(rates)
    mas = mas.lista()
    mas = mas[-1:]  # limita à última linha
    view = view_ma.MaView(mas)
    view = view.view()
    click.echo(view)


if __name__ == "__main__":
    ma()

"""Exibe a média móvel do indicador MA_TXT."""

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
@click.option("--date", "-d", help="Data no formato YYYY-MM-DD")
@click.option("--time", "-t", help="Horário no formato HH:MM")
def ma(symbol, period, count, date, time):
    """Exibe as medias moveis do indicador MA_TXT."""
    rates = model_rates_ma.RatesMaModel(symbol, period, count)
    rates = rates.lista()
    mas = model_mas.MasModel(rates)
    mas = mas.lista()
    view = view_ma.MaView(mas, date, time)
    view = view.view()
    click.echo(view)


if __name__ == "__main__":
    ma()

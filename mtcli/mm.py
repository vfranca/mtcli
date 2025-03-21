"""
Calcula a média móvel simples
"""

import click
from mtcli import csv_data
from mtcli.pa import bar as pa_bar
from mtcli import conf


@click.command()
@click.argument("symbol")
@click.option(
    "--period",
    "-p",
    type=click.Choice(
        [
            "mn1",
            "w1",
            "d1",
            "h4",
            "h3",
            "h2",
            "h1",
            "m30",
            "m20",
            "m15",
            "m12",
            "m10",
            "m6",
            "m5",
            "m4",
            "m3",
            "m2",
            "m1",
        ],
        case_sensitive=False,
    ),
    default="D1",
    help="Tempo grafico, default D1.",
)
@click.option("--count", "-c", default=20, help="Quantidade de barras, default 20.")
def mm(symbol, period, count):
    """Calcula a media movel simples."""
    fcsv = conf.csv_path + symbol + period + ".csv"
    prices = []
    rates = csv_data.get_data(fcsv)
    for rate in rates:
        bar = pa_bar.Bar(rate)
        prices.append(bar.close)
    prices = prices[-count:]
    sma = round(sum(prices) / len(prices), conf.digitos)
    click.echo(sma)


if __name__ == "__main__":
    mm()

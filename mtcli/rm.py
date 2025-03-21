"""
Calcula o tamanho médio das barras
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
@click.option("--count", "-c", default=10, help="Quantidade de barras, default 10.")
def rm(symbol, period, count):
    """Calcula o tamanho medio das barras."""
    fcsv = conf.csv_path + symbol + period + ".csv"
    ranges = []
    rates = csv_data.get_data(fcsv)
    for rate in rates:
        bar = pa_bar.Bar(rate)
        # Elimina doji de 4 preços
        if bar.open == bar.high and bar.high == bar.low and bar.low == bar.close:
            continue
        ranges.append(bar.high - bar.low)
    ranges = ranges[-count:]
    rm = round(sum(ranges) / len(ranges), conf.digitos)
    click.echo(rm)


if __name__ == "__main__":
    rm()

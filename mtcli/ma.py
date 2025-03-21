"""
Exibe a média móvel do indicador MA_TXT
"""

import click
from mtcli import csv_data
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
@click.option(
    "--count", "-c", type=int, default=20, help="Quantidade de barras, default 20."
)
def ma(symbol, period, count):
    """Exibe as medias moveis do indicador MA_TXT."""
    fcsv = conf.csv_path + symbol + period + "-MA" + str(count) + ".csv"
    ma_data = csv_data.get_data(fcsv)
    for ma in ma_data:
        click.echo("%s %s" % (ma[3], ma[2]))


if __name__ == "__main__":
    ma()

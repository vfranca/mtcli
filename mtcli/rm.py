"""
Exibe o range médio das barras
"""

import click
from mtcli import csv_data
from mtcli.pa import pa_bar
from mtcli import conf


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="D1", help="Tempo gráfico")
@click.option("--count", "-c", default=14, help="Quantidade de barras")
def rm(symbol, period, count):
    """Exibe o range médio das barras."""
    csv_file = conf.csv_path + symbol + period + ".csv"
    ranges = []
    rates = csv_data.get_data(csv_file)
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

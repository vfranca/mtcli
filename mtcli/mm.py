"""
Exibe a media móvel simples
"""
import click
from mtcli.csv_data import get_data
from mtcli.pa.pa_bar import Bar
from mtcli import conf


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="D1", help="Tempo gráfico")
@click.option("--count", "-c", default=20, help="Quantidade de barras")
def mm(symbol, period, count):
    """Exibe a media móvel simples."""
    csv_file = conf.csv_path + symbol + period + ".csv"
    prices = []
    rates = get_data(csv_file)
    for rate in rates:
        bar = Bar(rate)
        prices.append(bar.close)
    prices = prices[-count:]
    sma = round(sum(prices) / len(prices), conf.digits)
    click.echo(sma)


if __name__ == "__main__":
    mm()

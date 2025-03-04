"""
Exibe a média móvel do indicador MA_TXT
"""

import click
from mtcli import csv_data
from mtcli import conf


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="D1", help="Tempo gráfico.")
@click.option("--count", "-c", type=int, default=20, help="Quantidade de barras.")
def ma(symbol, period, count):
    """Exibe a media móvel do indicador MA_TXT."""
    # Arquivo CSV contendo as médias móveis
    csv_file = conf.csv_path + symbol + period + "-MA" + str(count) + ".csv"
    # Importa as médias móveis
    ma_data = csv_data.get_data(csv_file)
    for ma in ma_data:
        click.echo("%s %s" % (ma[3], ma[2]))


if __name__ == "__main__":
    ma()

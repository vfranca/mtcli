# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import click
from mtcli.csv_ma import MAs
from mtcli.conf import csv_path


# Cria o comando ma
@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="D1", help="Período aplicado.")
@click.option("--count", "-c", type=int, default=20, help="Quantidade de períodos.")
def ma(symbol, period, count):
    """Exibe as médias móveis do indicador MA_TXT."""
    # Arquivo CSV contendo as médias móveis
    csv_file = csv_path + symbol + period + "-MA" + str(count) + ".csv"
    # Importa as médias móveis
    mas = MAs(csv_file)
    for ma in mas:
        click.echo("%s %s" % (ma[3], ma[2]))


if __name__ == "__main__":
    ma()

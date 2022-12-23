import click
from mtcli.csv_data import Rates
from mtcli.pa.pa_bar import Bar
from mtcli import conf


# Cria o comando mm
@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="D1", help="Tempo gráfico")
@click.option("--count", "-c", default=20, help="Quantidade de períodos")
def mm(symbol, period, count):
    """Média móvel simples dos  preços de fechamento."""
    csv_file = conf.csv_path + symbol + period + ".csv"
    prices = []
    rates = Rates(csv_file)
    for rate in rates:
        bar = Bar(rate)
        prices.append(bar.close)
    prices = prices[-count:]
    sma = round(sum(prices) / len(prices), conf.digits)
    click.echo(sma)


if __name__ == "__main__":
    mm()

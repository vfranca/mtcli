import click
from mtcli.csv_data import Rates
from mtcli.pa.pa_bar import Bar
from mtcli import conf


# Cria o comando rm
@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="D1", help="Tempo gráfico")
@click.option("--count", "-c", default=14, help="Quantidade de períodos")
def rm(symbol, period, count):
    """Range médio das barras."""
    csv_file = conf.csv_path + symbol + period + ".csv"
    ranges = []
    rates = Rates(csv_file)
    for rate in rates:
        bar = Bar(rate)
        # Elimina doji de 4 preços
        if bar.open == bar.high and bar.high == bar.low and bar.low == bar.close:
            continue
        ranges.append(bar.high - bar.low)
    ranges = ranges[-count:]
    rm = round(sum(ranges) / len(ranges), conf.digits)
    click.echo(rm)


if __name__ == "__main__":
    rm()

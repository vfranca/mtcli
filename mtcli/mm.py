import click
from mtcli import indicator


# Cria o comando mm
@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="h1", help="Tempo gráfico")
@click.option("--count", "-c", default=20, help="Quantidade de períodos")
def mm(symbol, period, count):
    """Calcula a média móvel simples."""
    click.echo(indicator.sma.get_sma(symbol, period, count))


if __name__ == "__main__":
    mm()

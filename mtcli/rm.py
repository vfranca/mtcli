import click
from mtcli import indicator


# Cria o comando rm
@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="h1", help="Tempo gráfico")
@click.option("--count", "-c", default=14, help="Quantidade de períodos")
def rm(symbol, period, count):
    """Calcula o range médio das barras."""
    click.echo(indicator.atr.get_atr(symbol, period, count))


if __name__ == "__main__":
    rm()

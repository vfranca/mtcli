# -*- coding: utf-8 -*-
import click
from mtcli import indicator
from mtcli.mtcli import controller
from mtcli.fib import Fib


@click.group()
def cli():
    """Console de scripts para MTCLI."""
    pass


@click.command()
@click.argument("symbol")
@click.option(
    "--period", "-p", default="daily",
    help="Timeframe ou tempo gráfico")
@click.option("--view", "-v", help="Formato de exibição")
@click.option("--count", "-c", default=40, help="Quantidade de barras")
@click.option("--date", "-d", help="Data para day trade")
def bars(symbol, period, view, count, date):
    """Grafico de barras ou candles."""
    views = controller(symbol, period, view, date, count)
    for view in views:
        click.echo(view)


@click.command()
@click.argument("symbol")
@click.option(
    "--period", "-p", default="h1",
    help="Timeframe ou tempo gráfico")
@click.option(
    "--count", "-c", default=20,
    help="Quantidade de períodos abrangidos no cálculo")
def sma(symbol, period, count):
    """Média móvel aritmética."""
    click.echo(indicator.sma.get_sma(symbol, period, count))


@click.command()
@click.argument("symbol")
@click.option(
    "--period", "-p", default="h1",
    help="Timeframe ou tempo gráfico")
@click.option(
    "--count", "-c", default=20,
    help="Quantidade de períodos abrangidos no cálculo")
def ema(symbol, period, count):
    """ Média móvel exponencial."""
    click.echo(indicator.ema.get_ema(symbol, period, count))


@click.command()
@click.argument("symbol")
@click.option(
    "--period", "-p", default="h1",
    help="Timeframe ou tempo gráfico")
@click.option(
    "--count", "-c", default=14,
    help="Quantidade de períodos abrangidos no cálculo")
def atr(symbol, period, count):
    """Range médio."""
    click.echo(indicator.atr.get_atr(symbol, period, count))


@click.command()
@click.argument("high")
@click.argument("low")
@click.argument("trend")
def fib(high, low, trend):
    """Retrações e extensões de fibonacci."""
    click.echo(Fib(float(high), float(low), str(trend)))


cli.add_command(bars)
cli.add_command(sma)
cli.add_command(ema)
cli.add_command(atr)
cli.add_command(fib)


if __name__ == "__main__":
    exit(cli())

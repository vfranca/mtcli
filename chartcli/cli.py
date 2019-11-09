# -*- coding: utf-8 -*-
import sys
import click
from chartcli import conf
from chartcli import indicator
from chartcli.chartcli import controller
from chartcli.lib.fib import Fib


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="daily", help="Timeframe ou tempo gráfico")
@click.option("--view", "-v", help="Formato de exibição")
@click.option("--count", "-c", default=40, help="Quantidade de barras")
@click.option("--date", "-d", help="Data para day trade")
def bars(symbol, period, view, count, date):
    """ Exibe as barras do grafico."""
    views = controller(symbol, period, view, date, count)
    for view in views:
        click.echo(view)

@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="h1", help="Timeframe ou tempo gráfico")
@click.option("--count", "-c", default=20, help="Quantidade de períodos abrangidos no cálculo")
def sma(symbol, period, count):
    click.echo(indicator.sma.get_sma(symbol, period, count))

@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="h1", help="Timeframe ou tempo gráfico")
@click.option("--count", "-c", default=20, help="Quantidade de períodos abrangidos no cálculo")
def ema(symbol, period, count):
    """ Calcula a média móvel exponencial."""
    click.echo(indicator.ema.get_ema(symbol, period, count))

@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="h1", help="Timeframe ou tempo gráfico")
@click.option("--count", "-c", default=14, help="Quantidade de períodos abrangidos no cálculo")
def atr(symbol, period, count):
    """ Calcula o ATR."""
    click.echo(indicator.atr.get_atr(symbol, period, count))

@click.command()
@click.argument("high")
@click.argument("low")
@click.argument("trend")
def fib(high, low, trend):
    """ Calcula retrações e extensões de fibonacci."""
    click.echo(Fib(float(high), float(low), str(trend)))

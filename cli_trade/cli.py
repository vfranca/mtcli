# -*- coding: utf-8 -*-
import sys
import click
from cli_trade import conf
from cli_trade import indicator


@click.command()
@click.argument("asset")
@click.option("--view", help="Formato de exibição")
@click.option("--count", default=40, help="Quantidade de barras")
def bars(asset, view, count):
    for i in range(count):
        click.echo("%i %s %s" % (i+1, asset, view))

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

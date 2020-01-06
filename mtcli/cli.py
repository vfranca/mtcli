# -*- coding: utf-8 -*-
import click
from mtcli import indicator
from mtcli.mtcli import controller
from mtcli.fib import Fib
from mtcli import trading
from mtcli.conf import *


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


@click.command()
def info():
    """Exibe dados da conta."""
    click.echo(trading.info())
    return 0


@click.command()
@click.argument("symbol")
@click.option("--volume", "-v", default=VOLUME, help="Volume ou quantidade do ativo")
@click.option("--price", "-p", help="Preço de entrada da operação")
@click.option("--stop_loss", "-sl", default=STOP_LOSS, help="Preço de stop loss da operação")
@click.option("--take_profit", "-tp", default=TAKE_PROFIT, help="Preço de take profit ou stop gain da operação")
def buy(symbol, volume, price, stop_loss, take_profit):
    """Executa uma órdem de compra."""
    close = trading.get_close(symbol)
    if not price:
        ticket = trading.buy(symbol, volume)
    elif float(price) <= close:
        ticket = trading.buy_limit(symbol, float(price), int(volume), float(stop_loss), float(take_profit))
    elif float(price) > close:
        ticket = trading.buy_stop(symbol, float(price), int(volume), float(stop_loss), float(take_profit))
    click.echo(ticket)
    return 0


@click.command()
@click.argument("symbol")
@click.option("--volume", "-v", default=VOLUME, help="Volume ou quantidade do ativo")
@click.option("--price", "-p", help="Preço de entrada da operação")
@click.option("--stop_loss", "-sl", default=STOP_LOSS, help="Preço de stop loss da operação")
@click.option("--take_profit", "-tp", default=TAKE_PROFIT, help="Preço de take profit ou stop gain da operação")
def sell(symbol, volume, price, stop_loss, take_profit):
    """Executa uma órdem de venda."""
    close = trading.get_close(symbol)
    if not price:
        ticket = trading.sell(symbol, volume)
    elif float(price) >= close:
        ticket = trading.sell_limit(symbol, float(price), int(volume), float(stop_loss), float(take_profit))
    elif float(price) < close:
        ticket = trading.sell_stop(symbol, float(price), int(volume), float(stop_loss), float(take_profit))
    click.echo(ticket)
    return 0


@click.command()
@click.option("--symbol", "-s", help="Ativo objeto")
@click.option("--order", "-o", help="Ticket da órdem")
@click.option("--volume", "-v", help="Volume a reduzir")
@click.option("--stop_loss", "-sl", help="Novo stop loss")
@click.option("--take_profit", "-tp", help="Novo take profit")
@click.option("--cancel", "-c", default="n", help="Cancelar? s/n")
def positions(symbol, order, volume, stop_loss, take_profit, cancel):
    """Gerencia posições."""
    click.echo(trading.positions())
    return 0


@click.command()
@click.option("--order", "-o", help="Ticket da órdem a ser cancelada")
@click.option("--position", "-p", help="ID da posição a ser cancelada")
def cancel(order=None, position=None):
    """Cancela órdens e posições."""
    click.echo(trading.cancel_orders())
    click.echo(trading.cancel_positions())
    return 0


cli.add_command(bars)
cli.add_command(sma)
cli.add_command(ema)
cli.add_command(atr)
cli.add_command(fib)
cli.add_command(info)
cli.add_command(buy)
cli.add_command(sell)
cli.add_command(positions)
cli.add_command(cancel)


if __name__ == "__main__":
    exit(cli())

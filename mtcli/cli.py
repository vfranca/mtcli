# -*- coding: utf-8 -*-
import click
from mtcli import indicator, trading
from mtcli.mtcli import controller
from mtcli.fib import Fib
from mtcli.conf import ORDER_REFUSED


@click.group()
def cli():
    """Console de scripts para MTCLI."""
    pass


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="daily", help="Timeframe ou tempo gráfico")
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
@click.option("--period", "-p", default="h1", help="Timeframe ou tempo gráfico")
@click.option(
    "--count", "-c", default=20, help="Quantidade de períodos abrangidos no cálculo"
)
def sma(symbol, period, count):
    """Média móvel aritmética."""
    click.echo(indicator.sma.get_sma(symbol, period, count))


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="h1", help="Timeframe ou tempo gráfico")
@click.option(
    "--count", "-c", default=20, help="Quantidade de períodos abrangidos no cálculo"
)
def ema(symbol, period, count):
    """ Média móvel exponencial."""
    click.echo(indicator.ema.get_ema(symbol, period, count))


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="h1", help="Timeframe ou tempo gráfico")
@click.option(
    "--count", "-c", default=14, help="Quantidade de períodos abrangidos no cálculo"
)
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
@click.option("--volume", "-v", type=int, help="Volume ou quantidade do ativo")
@click.option("--price", "-p", type=float, help="Preço de entrada da operação")
@click.option("--stop_loss", "-sl", type=float, help="Preço de stop loss da operação")
@click.option(
    "--take_profit",
    "-tp",
    type=float,
    help="Preço de take profit ou stop gain da operação",
)
def buy(symbol, volume, price, stop_loss, take_profit):
    """Executa uma órdem de compra."""
    close = trading.get_close(symbol)
    if not price:
        res = trading.buy(symbol, volume, stop_loss, take_profit)
    elif price <= close:
        res = trading.buy_limit(symbol, price, volume, stop_loss, take_profit)
    elif price > close:
        res = trading.buy_stop(symbol, price, volume, stop_loss, take_profit)
    if not res:
        res = ORDER_REFUSED
    click.echo(res)
    return 0


@click.command()
@click.argument("symbol")
@click.option("--volume", "-v", type=int, help="Volume ou quantidade do ativo")
@click.option("--price", "-p", type=float, help="Preço de entrada da operação")
@click.option("--stop_loss", "-sl", type=float, help="Preço de stop loss da operação")
@click.option(
    "--take_profit",
    "-tp",
    type=float,
    help="Preço de take profit ou stop gain da operação",
)
def sell(symbol, volume, price, stop_loss, take_profit):
    """Executa uma órdem de venda."""
    close = trading.get_close(symbol)
    if not price:
        res = trading.sell(symbol, volume, stop_loss, take_profit)
    elif price >= close:
        res = trading.sell_limit(symbol, price, volume, stop_loss, take_profit)
    elif price < close:
        res = trading.sell_stop(symbol, price, volume, stop_loss, take_profit)
    if not res:
        res = ORDER_REFUSED
    click.echo(res)
    return 0


@click.command()
@click.option("--symbol", "-s", help="Ativo objeto")
@click.option("--ticket", "-t", type=int, help="Ticket da órdem")
@click.option("--cancel", "-c", help="Cancela todas as órdens pendentes")
def orders(symbol, ticket, cancel):
    """Gerencia as órdens pendentes."""
    click.echo(trading.get_orders())
    return 0


@click.command()
@click.option("--symbol", "-s", help="Ativo objeto")
@click.option("--ticket", "-t", type=int, help="Ticket da posição")
@click.option("--volume", "-v", type=int, help="Volume a reduzir")
@click.option("--stop_loss", "-sl", type=float, help="Novo stop loss")
@click.option("--take_profit", "-tp", type=float, help="Novo take profit")
@click.option("--cancel", "-c", help="Cancela todas as posições abertas")
def positions(symbol, ticket, volume, stop_loss, take_profit, cancel):
    """Gerencia as posições abertas."""
    click.echo(trading.get_positions())
    return 0


@click.command()
@click.option("--symbol", "-s", help="Ativo cuja posição será cancelada")
@click.option("--order", "-o", help="Ticket da órdem a ser cancelada")
@click.option("--position", "-p", help="Ticket da posição a ser cancelada")
def cancel(symbol, order, position):
    """Cancela órdens e posições."""
    res_orders = trading.cancel_orders()
    res_positions = trading.cancel_positions()
    res = ""
    if res_orders and res_positions:
        res = "Todas as órdens e posições foram canceladas com sucesso!"
    click.echo(res)
    return 0


cli.add_command(bars)
cli.add_command(sma)
cli.add_command(ema)
cli.add_command(atr)
cli.add_command(fib)
cli.add_command(info)
cli.add_command(buy)
cli.add_command(sell)
cli.add_command(orders)
cli.add_command(positions)
cli.add_command(cancel)


if __name__ == "__main__":
    exit(cli())

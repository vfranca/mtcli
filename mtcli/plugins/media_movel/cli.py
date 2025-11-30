"""Comando da médiamóvel."""

import click

from .conf import (
    LIMIT,
    LINHAS,
    PERIOD,
    TIMEFRAMES,
    TIPO_MM,
)
from .controller import obter_media_movel
from .view import exibir_media_movel


@click.command(
    "mm", help="Calcula a média móvel (SMA ou EMA) para o ativo e período especificado."
)
@click.argument("symbol")
@click.option(
    "--period",
    "-p",
    type=click.Choice(TIMEFRAMES, case_sensitive=False),
    default=PERIOD,
    show_default=True,
    help="Timeframe da media movel.",
)
@click.option(
    "--limit",
    "-l",
    default=LIMIT,
    show_default=True,
    help="Quantidade de timeframes da media movel.",
)
@click.option(
    "--tipo",
    "-t",
    default=TIPO_MM,
    show_default=True,
    type=click.Choice(["sma", "ema"]),
    help="Tipo da media.",
)
@click.option(
    "--linhas",
    "-li",
    type=int,
    default=LINHAS,
    show_default=True,
    help="Quantidade de linhas exibidas.",
)
@click.option(
    "--inicio",
    help="Data/hora inicial no formato YYYY-MM-DD ou YYYY-MM-DD HH:MM.",
)
@click.option(
    "--fim", help="Data/hora final no formato YYYY-MM-DD ou YYYY-MM-DD HH:MM."
)
def mm(symbol, period, limit, tipo, linhas, inicio, fim):
    """
    Calcula a média móvel (SMA ou EMA) do ativo SYMBOL.
    """
    resultado = obter_media_movel(
        symbol=symbol,
        period=period,
        limit=limit,
        tipo=tipo,
        inicio=inicio,
        fim=fim,
        linhas=linhas,
    )
    exibir_media_movel(resultado, linhas)


if __name__ == "__main__":
    mm()

"""Comando da médiamóvel."""

import click

from . import conf
from mtcli.logger import logger
from mtcli.models.model_rates import RatesModel
from .models import model_media_movel
from .views import view_media_movel


def calcular_sma(closes, window):
    closes = [float(c) for c in closes]
    return [
        sum(closes[i - window + 1 : i + 1]) / window
        for i in range(window - 1, len(closes))
    ]


def calcular_ema(closes, window):
    closes = [float(c) for c in closes]  # Garante que são números
    ema = []
    k = 2 / (window + 1)
    sma = sum(closes[:window]) / window
    ema.append(sma)
    for price in closes[window:]:
        ema.append(price * k + ema[-1] * (1 - k))
    return ema


@click.command()
@click.argument("symbol")
@click.option("--period", "-p", default="D1", help="Tempo gráfico.")
@click.option(
    "--periodos", type=int, default=20, help="Quantidade de períodos da média."
)
@click.option(
    "--tipo",
    default="sma",
    type=click.Choice(["sma", "ema"]),
    help="Tipo de média: sma ou ema.",
)
@click.option(
    "--limit", type=int, default=5, help="Limita a quantidade de linhas exibidas."
)
def mm(symbol, period, periodos, tipo, limit):
    """
    Calcula a média móvel (SMA ou EMA) do ativo SYMBOL no período PERIOD.
    """
    logger.info(
        f"Iniciando cálculo da média móvel: ativo {symbol} período {period} períodos {periodos} tipo {tipo} limite de exibição {limit} linhas."
    )
    rates = RatesModel(symbol, period).lista
    closes = [r[4] for r in rates]
    datas = [r[0] for r in rates]

    if len(closes) < periodos:
        logger.warning("Dados insuficientes para calcular a média.")
        click.echo("Dados insuficientes para calcular a média.")
        return

    if tipo == "sma":
        media = calcular_sma(closes, periodos)
        datas = datas[periodos - 1 :]
    else:
        media = calcular_ema(closes, periodos)
        datas = datas[periodos - 1 :]

    linhas = zip(datas, media)
    if limit > 0:
        linhas = list(linhas)[-limit:]

    for dt, valor in linhas:
        click.echo(f"{round(valor, conf.digitos)}    {dt}")

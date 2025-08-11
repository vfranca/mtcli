"""Comando da médiamóvel."""

import click

from . import conf
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
@click.option("--barras", type=int, default=20, help="Quantidade de barras da média.")
@click.option(
    "--tipo",
    default="sma",
    type=click.Choice(["sma", "ema"]),
    help="Tipo de média: sma ou ema.",
)
@click.option(
    "--limit", type=int, default=5, help="Limita a quantidade de linhas exibidas."
)
def mm(symbol, period, barras, tipo, limit):
    """
    Calcula a média móvel (SMA ou EMA) do ativo SYMBOL no período PERIOD.
    """
    rates = RatesModel(symbol, period).lista
    closes = [r[4] for r in rates]
    datas = [r[0] for r in rates]

    if len(closes) < barras:
        click.echo("Dados insuficientes para calcular a média.")
        return

    if tipo == "sma":
        media = calcular_sma(closes, barras)
        datas = datas[barras - 1 :]
    else:
        media = calcular_ema(closes, barras)
        datas = datas[barras - 1 :]

    linhas = zip(datas, media)
    if limit > 0:
        linhas = list(linhas)[-limit:]

    for dt, valor in linhas:
        click.echo(f"{round(valor, conf.digitos)}    {dt}")

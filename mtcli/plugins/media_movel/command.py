"""Comando da médiamóvel."""

from datetime import datetime

import click

from mtcli.logger import setup_logger
from mtcli.models.rates_model import RatesModel

from . import conf
from .models.model_media_movel import MediaMovelModel

logger = setup_logger()


@click.command(
    "mm", help="Calcula a média móvel (SMA ou EMA) para o ativo e período especificado."
)
@click.argument("symbol")
@click.option(
    "--period",
    "-p",
    type=click.Choice(conf.timeframes, case_sensitive=False),
    default="D1",
    help="Tempo gráfico, default D1.",
)
@click.option(
    "--periodos",
    "-pe",
    default=conf.periodos,
    help="Quantidade de períodos da média, default 14.",
)
@click.option(
    "--tipo",
    default="sma",
    type=click.Choice(["sma", "ema"]),
    help="Tipo de média sma ou ema; default sma.",
)
@click.option(
    "--limit",
    type=int,
    default=conf.limite_linhas,
    help="Limita a quantidade de linhas exibidas; default: 5.",
)
@click.option(
    "--inicio",
    type=str,
    help="Data/hora inicial no formato YYYY-MM-DD ou YYYY-MM-DD HH:MM.",
)
@click.option(
    "--fim", type=str, help="Data/hora final no formato YYYY-MM-DD ou YYYY-MM-DD HH:MM."
)
def mm(symbol, period, periodos, tipo, limit, inicio, fim):
    """
    Calcula a média móvel (SMA ou EMA) do ativo SYMBOL.
    """
    logger.info(
        f"Iniciando cálculo da média móvel: ativo {symbol} período {period} períodos {periodos} tipo {tipo} limite {limit}"
    )

    rates = RatesModel(symbol, period).get_data()
    closes = [r[4] for r in rates]
    datas = [r[0] for r in rates]

    if len(closes) < periodos:
        logger.warning("Dados insuficientes para calcular a média.")
        click.echo("Dados insuficientes para calcular a média.")
        return

    model_mm = MediaMovelModel(closes, periodos)
    if tipo == "sma":
        media = model_mm.calcula_sma()
    else:
        media = model_mm.calcula_ema()

    datas = datas[periodos - 1 :]

    # Filtro por data/hora
    dt_inicio = datetime.fromisoformat(inicio) if inicio else None
    dt_fim = datetime.fromisoformat(fim) if fim else None

    # formato compatível com '2023.08.31 00:00:00'
    formato = "%Y.%m.%d %H:%M:%S"

    filtrado = []
    for d, m in zip(datas, media):
        dt = datetime.strptime(d, formato)
        if (not dt_inicio or dt >= dt_inicio) and (not dt_fim or dt <= dt_fim):
            filtrado.append((d, m))

    if not filtrado:
        click.echo("Nenhum dado no intervalo especificado.")
        return

    if limit > 0:
        filtrado = filtrado[-limit:]

    for dt, valor in filtrado:
        click.echo(f"{round(valor, conf.digitos)}    {dt}")

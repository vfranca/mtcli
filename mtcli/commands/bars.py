"""Exibe o gráfico de barras."""

import click

from mtcli import conf
from mtcli.models.rates_model import RatesModel
from mtcli.models.bars_model import BarsModel
from mtcli.views import (
    view_close,
    view_full,
    view_high,
    view_low,
    view_min,
    view_open,
    view_ranges,
    view_rates,
    view_vars,
    view_volumes,
)
from mtcli.logger import setup_logger

logger = setup_logger("mtcli")  # Cria o logger


@click.command(
    "bars",
    help="Mostra o gráfico de candles em texto para o ativo e período especificados.",
)
@click.argument("symbol")
@click.option(
    "--view",
    "-v",
    type=click.Choice(
        [
            "ch",
            "m",
            "hl",
            "f",
            "full",
            "r",
            "range",
            "v",
            "volume",
            "va",
            "percentual",
            "oh",
            "ohlc",
            "o",
            "open",
            "h",
            "high",
            "l",
            "low",
            "c",
            "close",
        ],
        case_sensitive=False,
    ),
    default=conf.view,
    help="Formato de exibicao, default m. Opcoes: ch ou m - minima; f - completa; r - ranges; v - volumes; va - variações percentuais; oh - OHLC; o - aberturas; h - maximas; l - minimas; c - fechamentos",
)
@click.option(
    "--period",
    "-p",
    type=click.Choice(conf.timeframes, case_sensitive=False),
    default=conf.period,
    help="Tempo grafico, default D1.",
)
@click.option(
    "--count",
    "-c",
    type=int,
    default=conf.periodos,
    help="Quantidade de barras, default 20.",
)
@click.option(
    "--date", "-d", default=conf.date, help="Data para intraday, formato AAAA-MM-DD."
)
@click.option("--numerator", "-n", is_flag=True, help="Ativa a numeracao das barras.")
@click.option("--show-date", "-sd", is_flag=True, help="Ativa a datacao das barras.")
@click.option(
    "--volume",
    "-vo",
    type=click.Choice(["tick", "real"], case_sensitive=False),
    default=conf.volume,
    help="Tipo de volume, default tick.",
)
def bars(symbol, view, period, count, date, numerator, show_date, volume):
    """Exibe o grafico do MetaTrader 5."""
    period = period.lower()
    view = view.lower()
    logger.info(
        f"Iniciando exibição do gráfico MT5: {symbol} view {view} no {period} data {date} numerador {numerator} data {show_date} volume {volume}."
    )
    rates = RatesModel(symbol, period, count).get_data()
    bars = BarsModel(rates, date).get_bars()
    views = []
    if view in ["m", "ch", "hl"]:  # máximas e mínimas
        views = view_min.MinView(
            bars, count, period, date, numerator, show_date
        ).views()
    elif view in ["r", "range"]:  # ranges
        views = view_ranges.RangesView(
            bars, count, period, date, numerator, show_date
        ).views()
    elif view in ["oh", "ohlc"]:  # OHLC
        views = view_rates.RatesView(
            bars, count, period, date, numerator, show_date
        ).views()
    elif view in ["va", "percentual"]:  # variações percentuais
        views = view_vars.VarsView(
            bars, count, period, date, numerator, show_date
        ).views()
    elif view in ["o", "open"]:  # abertura
        views = view_open.OpenView(
            bars, count, period, date, numerator, show_date
        ).views()
    elif view in ["h", "high"]:  # máximas
        views = view_high.HighView(
            bars, count, period, date, numerator, show_date
        ).views()
    elif view in ["l", "low"]:  # mínimas
        views = view_low.LowView(
            bars, count, period, date, numerator, show_date
        ).views()
    elif view in ["c", "close"]:  # fechamentos
        views = view_close.CloseView(
            bars, count, period, date, numerator, show_date
        ).views()
    elif view in ["v", "volume"]:  # volumes
        views = view_volumes.VolumesView(
            bars, count, period, date, numerator, show_date, volume
        ).views()
    else:  # completo
        views = view_full.FullView(
            bars, count, period, date, numerator, show_date
        ).views()
    if views:
        for view in views:
            click.echo(view)
    logger.info("Exibição do gráfico MT5 finalizada.")


if __name__ == "__main__":
    bars()

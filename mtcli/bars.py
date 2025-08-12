"""Exibe o gráfico de barras."""

import click

from mtcli import conf
from mtcli.logger import logger
from mtcli.models import model_bars, model_rates
from mtcli.views import (view_close, view_full, view_high, view_low, view_min,
                         view_open, view_ranges, view_rates, view_vars,
                         view_volumes)


@click.command()
@click.argument("symbol")
@click.option(
    "--view",
    "-v",
    type=click.Choice(
        ["ch", "m", "f", "r", "v", "va", "oh", "o", "h", "l", "c"],
        case_sensitive=False,
    ),
    default="m",
    help="Forma de exibicao, default m. Opcoes: ch ou m - minima; f - completa; r - ranges; v - volumes; va - variações percentuais; oh - OHLC; o - aberturas; h - maximas; l - minimas; c - fechamentos",
)
@click.option(
    "--period",
    "-p",
    type=click.Choice(conf.timeframes, case_sensitive=False),
    default="d1",
    help="Tempo grafico, default D1.",
)
@click.option(
    "--count", "-c", type=int, default=20, help="Quantidade de barras, default 20."
)
@click.option("--date", "-d", help="Data para intraday, formato AAAA-MM-DD.")
@click.option("--numerator", "-n", is_flag=True, help="Ativa a numeracao das barras.")
@click.option("--show-date", "-sd", is_flag=True, help="Ativa a datacao das barras.")
@click.option(
    "--volume",
    "-vo",
    type=click.Choice(["tick", "real"], case_sensitive=False),
    default="tick",
    help="Tipo de volume, default tick.",
)
def bars(symbol, view, period, count, date, numerator, show_date, volume):
    """Exibe o grafico do MetaTrader 5."""
    period = period.lower()
    view = view.lower()
    logger.info(
        f"Iniciando exibição do gráfico MT5: {symbol} view {view} no {period} data {date} numerador {numerator} data {show_date} volume {volume}."
    )
    rates = model_rates.RatesModel(symbol, period).lista
    bars = model_bars.BarsModel(rates, date).lista
    views = []
    if view == "m" or view == "ch":  # minimo
        views = view_min.MinView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "r":  # ranges
        views = view_ranges.RangesView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "oh":  # OHLC
        views = view_rates.RatesView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "va":  # variações percentuais
        views = view_vars.VarsView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "o":  # abertura
        views = view_open.OpenView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "h":  # máximas
        views = view_high.HighView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "l":  # mínimas
        views = view_low.LowView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "c":  # fechamentos
        views = view_close.CloseView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "v":  # volumes
        views = view_volumes.VolumesView(
            bars, count, period, date, numerator, show_date, volume
        )
        views = views.views()
    else:  # completo
        views = view_full.FullView(bars, count, period, date, numerator, show_date)
        views = views.views()
    if views:
        for view in views:
            click.echo(view)
    logger.info("Exibição do gráfico MT5 finalizada.")


if __name__ == "__main__":
    bars()

"""Exibe o gráfico de barras."""

import click

from mtcli.conf import (
    DATE,
    PERIOD,
    PERIODOS,
    SYMBOL,
    TIMEFRAMES,
    VIEW,
    VOLUME,
)
from mtcli.models.bars_model import BarsModel
from mtcli.models.rates_model import RatesModel
from mtcli.views.close_view import CloseView
from mtcli.views.full_view import FullView
from mtcli.views.high_view import HighView
from mtcli.views.low_view import LowView
from mtcli.views.min_view import MinView
from mtcli.views.open_view import OpenView
from mtcli.views.ranges_view import RangesView
from mtcli.views.rates_view import RatesView
from mtcli.views.vars_view import VarsView
from mtcli.views.volumes_view import VolumesView


@click.command(
    help="Mostra o gráfico de candles em texto para o ativo e período especificados.",
)
@click.option(
    "--symbol",
    "-s",
    default=SYMBOL,
    show_default=True,
    help="Codigo ou ticker do ativo.",
)
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
    default=VIEW,
    show_default=True,
    help="Formato de exibicao. Opcoes: minima ou HL - minima; f - completa; r - ranges; v - volumes; va - variações percentuais; oh - OHLC; o - aberturas; h - maximas; l - minimas; c - fechamentos.",
)
@click.option(
    "--period",
    "-p",
    type=click.Choice(TIMEFRAMES, case_sensitive=False),
    default=PERIOD,
    show_default=True,
    help="Timeframe do grafico.",
)
@click.option(
    "--count",
    "-c",
    type=int,
    default=PERIODOS,
    show_default=True,
    help="Quantidade de periodos a serem exibidos.",
)
@click.option(
    "--date",
    "-d",
    default=DATE,
    show_default=True,
    help="Data para intraday, formato AAAA-MM-DD.",
)
@click.option(
    "--numerator",
    "-n",
    is_flag=True,
    default=False,
    show_default=True,
    help="Ativa a numeracao das barras.",
)
@click.option(
    "--show-date",
    "-sd",
    is_flag=True,
    default=False,
    show_default=True,
    help="Ativa a datacao das barras.",
)
@click.option(
    "--volume",
    "-vo",
    type=click.Choice(["tick", "real"], case_sensitive=False),
    default=VOLUME,
    show_default=True,
    help="Tipo de volume.",
)
def bars(symbol, view, period, count, date, numerator, show_date, volume):
    """Exibe o grafico do MetaTrader 5."""
    period = period.lower()
    view = view.lower()
    rates = RatesModel(symbol, period, count).get_data()
    bars = BarsModel(rates, date).get_bars()
    views = []
    if view in ["m", "ch", "hl"]:  # máximas e mínimas
        views = MinView(bars, count, period, date, numerator, show_date).views()
    elif view in ["r", "range"]:  # ranges
        views = RangesView(bars, count, period, date, numerator, show_date).views()
    elif view in ["oh", "ohlc"]:  # OHLC
        views = RatesView(bars, count, period, date, numerator, show_date).views()
    elif view in ["va", "percentual"]:  # variações percentuais
        views = VarsView(bars, count, period, date, numerator, show_date).views()
    elif view in ["o", "open"]:  # abertura
        views = OpenView(bars, count, period, date, numerator, show_date).views()
    elif view in ["h", "high"]:  # máximas
        views = HighView(bars, count, period, date, numerator, show_date).views()
    elif view in ["l", "low"]:  # mínimas
        views = LowView(bars, count, period, date, numerator, show_date).views()
    elif view in ["c", "close"]:  # fechamentos
        views = CloseView(bars, count, period, date, numerator, show_date).views()
    elif view in ["v", "volume"]:  # volumes
        views = VolumesView(
            bars, count, period, date, numerator, show_date, volume
        ).views()
    else:  # completo
        views = FullView(bars, count, period, date, numerator, show_date).views()
    if views:
        for view in views:
            click.echo(view)


if __name__ == "__main__":
    bars()

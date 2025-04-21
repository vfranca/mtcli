"""
Exibe o gráfico de velas
"""

import click
from mtcli.views import view_full
from mtcli.views import view_intermediate
from mtcli.views import view_min
from mtcli.views import view_ranges
from mtcli.views import view_ranges
from mtcli.views import view_volumes
from mtcli.views import view_vars
from mtcli.views import view_rates
from mtcli.views import view_open
from mtcli.views import view_high
from mtcli.views import view_low
from mtcli.views import view_close
from mtcli import views as _views
from mtcli import conf
from mtcli.models import model_rates
from mtcli.models import model_bars


@click.command()
@click.argument("symbol")
@click.option(
    "--view",
    "-v",
    type=click.Choice(
        ["ch", "f", "i", "r", "var", "vol", "oh", "o", "h", "l", "c"],
        case_sensitive=False,
    ),
    default="f",
    help="Forma de exibicao, default f. Opcoes: ch - minima; f - completa; i - intermediaria; r - ranges; -var - variacoes percentuais; vol - volumes; oh - OHLC; o - aberturas; h - maximas; l - minimas; c - fechamentos",
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
@click.option("--numerator", "-n", is_flag=True, help="Ativa a numeracao das velas.")
@click.option("--show-date", "-sd", is_flag=True, help="Ativa a datacao das velas.")
def bars(symbol, view, period, count, date, numerator, show_date):
    """Exibe o grafico de velas."""
    period = period.lower()
    view = view.lower()
    rates = model_rates.RatesModel(symbol, period)
    rates = rates.lista
    bars = model_bars.BarsModel(rates, date)
    bars = bars.lista
    views = []
    if view == "ch":
        views = view_min.MinView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "r":
        views = view_ranges.RangesView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "oh":
        views = view_rates.RatesView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "var":
        views = view_vars.VarsView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "o":  # abertura
        views = view_open.OpenView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "h":
        views = view_high.HighView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "l":
        views = view_low.LowView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "c":
        views = view_close.CloseView(bars, count, period, date, numerator, show_date)
        views = views.views()
    elif view == "vol":
        views = view_volumes.VolumesView(
            bars, count, period, date, numerator, show_date
        )
        views = views.views()
    elif view == "i":
        views = view_intermediate.IntermediateView(
            bars, count, period, date, numerator, show_date
        )
        views = views.views()
    else:
        views = view_full.FullView(bars, count, period, date, numerator, show_date)
        views = views.views()
    if views:
        for view in views:
            click.echo(view)


if __name__ == "__main__":
    bars()

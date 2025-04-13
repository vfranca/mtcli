"""
Exibe o gráfico de velas
"""

import click
from mtcli.views import view_min
from mtcli.views import view_ranges
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
        ["ch", "f", "r", "var", "vol", "ohlc", "o", "h", "l", "c"], case_sensitive=False
    ),
    default="f",
    help="Forma de exibicao, default f.",
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
    elif view == "ohlc":
        views = _views.view_ohlc(bars, count, date, numerator)
    elif view == "var":
        views = _views.view_var(bars, count, period, date, numerator, show_date)
    elif view == "o":  # abertura
        views = _views.view_open(bars, count, period, date, numerator, show_date)
    elif view == "h":
        views = _views.view_high(bars, count, period, date, numerator, show_date)
    elif view == "l":
        views = _views.view_low(bars, count, period, date, numerator, show_date)
    elif view == "c":
        views = _views.view_close(bars, count, period, date, numerator, show_date)
    elif view == "vol":
        views = _views.view_volume(bars, count, period, date, numerator, show_date)
    else:
        views = _views.view_full(bars, count, period, date, numerator, show_date)
    if views:
        for view in views:
            click.echo(view)


if __name__ == "__main__":
    bars()

"""
Exibe o gráfico de barras
"""

import click
from mtcli import views as _views
from mtcli import csv_data
from mtcli import conf
from mtcli.pa import bar as pa_bar


@click.command()
@click.argument("symbol")
@click.option("--view", "-v", default="ch", help="Forma de exibicao default ch")
@click.option("--period", "-p", default="d1", help="Tempo grafico default D1")
@click.option(
    "--count", "-c", type=int, default=20, help="Quantidade de barras default 20"
)
@click.option("--date", "-d", help="Data para intraday")
@click.option("--num", "-n", is_flag=True)
def bars(symbol, view, period, count, date, num):
    """Exibe o gráfico de barras."""
    fcsv = conf.csv_path + symbol + period + ".csv"
    rates = csv_data.get_data(fcsv)
    bars = []
    for rate in rates:
        bar = pa_bar.Bar(rate)
        if date and bar.date != date:  # filtra por data para intraday
            num = True  # Configura numerador padrão para intraday
            continue
        bars.append(bar)
    views = []
    if view == "ch":
        views = _views.view_min(bars, count, num)
    elif view == "r":
        views = _views.view_ranges(bars, count, num)
    elif view == "ohlc":
        views = _views.view_ohlc(bars, count, num)
    elif view == "var":
        views = _views.view_var(bars, count, num)
    elif view == "o":
        views = _views.view_open(bars, count, num)
    elif view == "h":
        views = _views.view_high(bars, count, num)
    elif view == "l":
        views = _views.view_low(bars, count, num)
    elif view == "c":
        views = _views.view_close(bars, count, num)
    elif view == "vol":
        views = _views.view_volume(bars, count, num)
    else:
        views = _views.view_full(bars, count, num)
    if views:
        for view in views:
            click.echo(view)


if __name__ == "__main__":
    bars()

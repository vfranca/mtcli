import click
from mtcli.csv_data import Rates
from mtcli import views as _view
from mtcli.pa import helpers as helper
from mtcli.pa.pa_bar import Bar
from mtcli.pa.pa_one_bar import OneBar
from mtcli.pa.pa_two_bars import TwoBars
from mtcli import conf


# Cria o comando bars
@click.command()
@click.argument("symbol")
@click.option("--view", "-v", help="Formato de exibição")
@click.option("--period", "-p", default="D1", help="Tempo gráfico")
@click.option("--count", "-c", type=int, default=40, help="Quantidade de barras")
@click.option("--date", "-d", default="", help="Data (para day trade)")
def bars(symbol, view, period, count, date):
    """Lista as barras do gráfico."""

    """Retorna uma lista de barras."""
    # Arquivo CSV com as cotações OHLC
    csv_file = conf.csv_path + symbol + period + ".csv"

    # Inicia as variaveis
    views = []
    close = []
    open = []
    high1 = []
    low1 = []
    body = []
    num_bar = 0
    counter = 0
    bull = 0
    bear = 0
    doji = 0

    # Obtem as cotacoes (rates) do arquivo CSV
    rates = Rates(csv_file)
    for rate in rates:
        # Extrai os dados da barra
        bar = Bar(rate)
        counter += 1

        # Se houver uma data de intraday filtra a lista de barras a partir de uma data
        if date and bar.date != date:
            continue

        # Se houver um filtro por data obtem o número da barra
        if date:
            num_bar += 1
        else:
            num_bar = ""

        # Extrai o price action de 2 barras em sequência
        body.append(bar.body)
        open.append(bar.open)
        close.append(bar.close)
        high1.append(bar.high)
        low1.append(bar.low)
        if len(body) == 2:
            brooks = TwoBars(body, open, close, high1, low1)
            pattern2 = brooks.pattern
            ch_trend = brooks.trend
            var_close = helper.get_var(close[0], close[1])
            body.pop(0)
            open.pop(0)
            close.pop(0)
            high1.pop(0)
            low1.pop(0)
        else:
            pattern2 = ""
            ch_trend = ""
            var_close = ""

        # Contagem de barras de tendência e barras doji
        if count:
            start = len(rates) - count
            if counter > start:
                mp = helper.get_medium_point(bar)
                pattern1 = OneBar(bar.body, bar.top, bar.bottom, bar.close, mp)
                if pattern1.pattern == conf.lbl_buy_pressure:
                    bull += 1
                elif pattern1.pattern == conf.lbl_sell_pressure:
                    bear += 1
                else:
                    doji += 1

        # Seleção da view
        if view == "ohlc":
            views.append(_view.ohlc_view(bar))
        elif view == "ch":
            views.append(_view.channel_view(bar, ch_trend, num_bar))
        elif view == "c":
            views.append(_view.close_view(bar, num_bar))
        elif view == "h":
            views.append(_view.high_view(bar, num_bar))
        elif view == "l":
            views.append(_view.low_view(bar, num_bar))
        elif view == "r":
            views.append(_view.range_view(bar, ch_trend, num_bar))
        elif view == "vol":
            views.append(_view.volume_view(bar, ch_trend, num_bar))
        elif view == "stat":
            views = [_view.stat_view(bull, bear, doji)]
        elif view == "var":
            views.append(_view.var_view(ch_trend, var_close, num_bar))
        else:
            views.append(_view.brooks_view(bar, ch_trend, num_bar, pattern2, var_close))

        # Limita a quantidade de views
        if count and len(views) > count:
            views.pop(0)

    # Exibe as barras
    for view in views:
        click.echo(view)


if __name__ == "__main__":
    bars()

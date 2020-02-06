from mtcli.models import BarModel
from mtcli import views as _view
from mtcli import helpers as helper
from mtcli.bar import Bar
from mtcli.brooks_patterns1 import BrooksPatterns1
from mtcli.brooks_patterns2 import BrooksPatterns2
from mtcli import conf


def controller(
    symbol: str, period: str, view: str, date: str = "", count: int = 40
) -> list:
    """Retorna uma lista de views."""
    csv_file = conf.csv_path + symbol + period + ".csv"
    views, close, open = [], [], []
    high1, low1, body = [], [], []
    num_bar, counter, bull, bear, doji = 0, 0, 0, 0, 0

    bars = BarModel(csv_file)
    for item in bars:
        bar = Bar(item)
        counter += 1

        # Filtra a lista de views a partir de uma data
        if date and bar.date != date:
            continue

        # Obtem o número da barra
        if date:
            num_bar += 1
        else:
            num_bar = ""

        # Extrai dados de duas barras consecutivas
        body.append(bar.body)
        open.append(bar.open)
        close.append(bar.close)
        high1.append(bar.high)
        low1.append(bar.low)
        if len(body) == 2:
            brooks = BrooksPatterns2(body, open, close, high1, low1)
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
            start = len(bars) - count
            if counter > start:
                mp = helper.get_medium_point(bar)
                pattern1 = BrooksPatterns1(bar.body, bar.top, bar.bottom, bar.close, mp)
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

    return views

"""
Exibe o gráfico de barras
"""
import click
from mtcli import csv_data
from mtcli import conf
from mtcli import paction as pa


@click.command()
@click.argument("symbol")
@click.option("--view", "-v", help="Formato de exibição")
@click.option("--period", "-p", default="D1", help="Tempo gráfico")
@click.option("--count", "-c", type=int, default=40, help="Quantidade de barras")
@click.option("--date", "-d", help="Data para intraday")
def bars(symbol, view, period, count, date):
    """Exibe o grafico de barras."""
    # Arquivo CSV das cotações
    csv_file = conf.csv_path + symbol + period + ".csv"
    # Importa os dados CSV
    list_rates = csv_data.get_data(csv_file)
    # Restringe a N últimas barras
    list_rates = list_rates[-count:]
    # Converte a lista para dicionário
    dict_rates = {}
    for i in range(len(list_rates)):
        dict_rates[list_rates[i][0]] = list_rates[i][1:]
    # Prepara a string de exibição no formato mínimo
    # ASC 35.00 30.00 32.50
    view_min = "%s %.{0}f %.{0}f %.{0}f".format(conf.digits)
    # Prepara a string de exibição no formato ranges
    # ASC 5.00
    view_ranges = "%s %.{0}f".format(conf.digits)
    # Prepara a string de exibição no formato fechamentos
    # 32.50
    view_closes = "%.{0}f".format(conf.digits)
    # Prepara a string de exibição no formato variações percentuais
    # ASC 1.50%
    view_percentuais = "%s %.2f%%"
    # Prepara a string de exibição no formato completo
    # ASC CP VERDE75 G2.5 BOTTOM20 35.00 30.00 32.00M32.50 5.00 2.50%
    view_full = "%s %s %s%i %s %s %.{0}f %.{0}f %.{0}fM%.{0}f".format(conf.digits)
    # Definições em barras consecutivas
    list_h = []
    list_l = []
    list_c = []
    for k, v in dict_rates.items():
        h = float(v[1])
        l = float(v[2])
        c = float(v[3])
        # Obtem os preços consecutivos
        list_h.append(h)
        list_l.append(l)
        list_c.append(c)
        if len(list_h) == 2:
            # Define o tipo da barra
            barra = pa.tipo_barra(list_h, list_l)
            # Calcula o gap de fechamento
            gap = pa.gap_fechamento(list_c, list_h, list_l)
            # Calcula a variação percentual
            vp = pa.variacao_percentual(list_c)
            list_h.pop(0)
            list_l.pop(0)
            list_c.pop(0)
        else:
            barra = ""
            gap = ""
            vp = ""
        # Adiciona o tipo da barra ao dicionário de cotações
        dict_rates[k].append(barra)
        # Adiciona o gap de fechamento ao dicionário de cotações
        dict_rates[k].append(gap)
        # Adiciona a variação percentual ao dicionário de cotações
        dict_rates[k].append(vp)
    # Exibe as barras no formato mínimo
    if view and view.lower() == "ch":
        for v in dict_rates.values():
            click.echo(view_min % (v[6].upper(), float(v[1]), float(v[2]), float(v[3])))
        return 0
    # Exibe as barras no formato ranges
    if view and view.lower() == "r":
        f_range = 0
        for v in dict_rates.values():
            h, l = float(v[1]), float(v[2])
            f_range = pa.range_barra(h, l)
            click.echo(view_ranges % (v[6].upper(), f_range))
        return 0
    # Exibe as barras no formato completo
    for v in dict_rates.values():
        # Define os preços de abertura, máxima, mínima e fechamento
        o, h, l, c = float(v[0]), float(v[1]), float(v[2]), float(v[3])
        # Calcula o range do corpo
        range_body = c - o
        # Define a tendência da barra
        trend_bar = "doji"
        if range_body > 0:
            trend_bar = "verde"
        if range_body < 0:
            trend_bar = "vermelho"
        # Calcula o range da barra
        range_bar = h - l
        # Calcula o percentual de corpo
        percentual_body = abs(range_body) / range_bar * 100
        # Verifica se é uma barra de rompimento
        breakout = ""
        if percentual_body >= 60:
            breakout = "BO"
        click.echo(
            view_full
            % (
                v[6].upper(),
                breakout.upper(),
                trend_bar.upper(),
                percentual_body,
                v[7].upper(),
                "BOTTOM10".upper(),
                h,
                l,
                c,
                18.34,
            )
        )


if __name__ == "__main__":
    bars()

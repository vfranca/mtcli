"""Gerencia configurações registradas no mtcli.ini."""

import os

import click
import dotenv
import MetaTrader5 as mt5
from mtcli.conecta import conectar, shutdown


fconf = "mtcli.ini"
dotenv.load_dotenv(fconf)

default = {
    "digitos": "2",
    "lateral": "DOJI",
    "alta": "VERDE",
    "baixa": "VERMELHO",
    "rompimento_alta": "C",
    "rompimento_baixa": "V",
    "percentual_rompimento": "50",
    "percentual_doji": "10",
    "up_bar": "ASC",
    "down_bar": "DESC",
    "inside_bar": "IB",
    "outside_bar": "OB",
    "sombra_superior": "TOP",
    "sombra_inferior": "BOT",
    "gap": "G",
    "ponto_medio": "M",
    "dados": "MT5",
    "mt5_pasta": "",
}

digitos = int(os.getenv("DIGITOS", default["digitos"]))
lateral = os.getenv("LATERAL", default["lateral"])
alta = os.getenv("ALTA", default["alta"])
baixa = os.getenv("BAIXA", default["baixa"])
rompimento_alta = os.getenv("ROMPIMENTO_ALTA", default["rompimento_alta"])
rompimento_baixa = os.getenv("ROMPIMENTO_BAIXA", default["rompimento_baixa"])
percentual_rompimento = int(
    os.getenv("PERCENTUAL_ROMPIMENTO", default["percentual_rompimento"])
)
percentual_doji = int(os.getenv("PERCENTUAL_DOJI", default["percentual_doji"]))
up_bar = os.getenv("UP_BAR", default["up_bar"])
down_bar = os.getenv("DOWN_BAR", default["down_bar"])
inside_bar = os.getenv("INSIDE_BAR", default["inside_bar"])
outside_bar = os.getenv("OUTSIDE_BAR", default["outside_bar"])
gap = os.getenv("GAP", default["gap"])
sombra_superior = os.getenv("SOMBRA_SUPERIOR", default["sombra_superior"])
sombra_inferior = os.getenv("SOMBRA_INFERIOR", default["sombra_inferior"])
ponto_medio = os.getenv("PONTO_MEDIO", default["ponto_medio"])
data_source = os.getenv("DADOS", default["dados"]).upper()
csv_path = os.getenv("MT5_PASTA", default["mt5_pasta"])


def get_data_source():
    from mtcli.data import CsvDataSource, MT5DataSource

    if data_source == "CSV":
        return CsvDataSource()
    elif data_source == "MT5":
        return MT5DataSource()
    else:
        raise ValueError(f"Fonte de dados desconhecida: {data_source}")


if not csv_path:
    conectar()
    terminal_info = mt5.terminal_info()
    if terminal_info is None:
        raise RuntimeError("Não foi possível obter as informações do terminal.")

    csv_path = terminal_info.data_path + "/MQL5/Files"
    shutdown()

csv_path = csv_path.replace("\\", "/")
csv_path += "/"

timeframes = [
    "mn1",
    "w1",
    "d1",
    "h12",
    "h8",
    "h6",
    "h4",
    "h3",
    "h2",
    "h1",
    "m30",
    "m20",
    "m15",
    "m12",
    "m10",
    "m6",
    "m5",
    "m4",
    "m3",
    "m2",
    "m1",
]


@click.command()
@click.option("--digitos", "-d", help="Digitos da moeda, default 2.")
@click.option("--lateral", "-l", help="Nome da barra doji, default DOJI.")
@click.option("--alta", "-a", help="Nome da barra de alta, default VERDE.")
@click.option("--baixa", "-b", help="Nome da barra de baixa, default VERMELHO.")
@click.option(
    "--rompimento-alta", "-ra", help="Barra de rompimento de alta, default C."
)
@click.option(
    "--rompimento-baixa", "-rb", help="Barra de rompimento de baixa, default V."
)
@click.option("--sombra_superior", "-ss", help="Sombra superior, default TOP.")
@click.option("--sombra_inferior", "-si", help="Sombra inferior, default BOTTOM.")
@click.option("--ponto_medio", "-pm", help="Ponto medio da barra, default M.")
@click.option(
    "--percentual-doji", "-pd", help="Percentual do corpo da barra doji, default 10."
)
@click.option(
    "--percentual-rompimento",
    "-pr",
    help="Percentual do corpo da barra de rompimento, default 50.",
)
@click.option("--dados", "-da", help="Fonte dos dados.")
@click.option("--mt5-pasta", "-mp", help="Caminho da pasta do MetaTrader 5.")
def conf(**kwargs):
    """Gerencia configuracoes registradas no mtcli.ini."""
    res = False
    # dígitos da moeda
    if kwargs["digitos"]:
        res = dotenv.set_key(fconf, "DIGITOS", kwargs["digitos"])
    # nome da barra lateral
    if kwargs["lateral"]:
        res = dotenv.set_key(fconf, "LATERAL", kwargs["lateral"].upper())
    # nome da barra de alta
    if kwargs["alta"]:
        res = dotenv.set_key(fconf, "ALTA", kwargs["alta"].upper())
    # nome da barra de baixa
    if kwargs["baixa"]:
        res = dotenv.set_key(fconf, "BAIXA", kwargs["baixa"].upper())
    # abreviatura da barra de rompimento de alta
    if kwargs["rompimento_alta"]:
        res = dotenv.set_key(
            fconf, "ROMPIMENTO_ALTA", kwargs["rompimento_alta"].upper()
        )
    # abreviatura da barra de rompimento de baixa
    if kwargs["rompimento_baixa"]:
        res = dotenv.set_key(
            fconf, "ROMPIMENTO_BAIXA", kwargs["rompimento_baixa"].upper()
        )
    # sombra superior
    if kwargs["sombra_superior"]:
        res = dotenv.set_key(
            fconf, "SOMBRA_SUPERIOR", kwargs["sombra_superior"].upper()
        )
    # sombra inferior
    if kwargs["sombra_inferior"]:
        res = dotenv.set_key(
            fconf, "SOMBRA_INFERIOR", kwargs["sombra_inferior"].upper()
        )
    # ponto médio
    if kwargs["ponto_medio"]:
        res = dotenv.set_key(fconf, "PONTO_MEDIO", kwargs["ponto_medio"].upper())
    # percentual do corpo da barra doji
    if kwargs["percentual_doji"]:
        res = dotenv.set_key(fconf, "PERCENTUAL_DOJI", kwargs["percentual_doji"])
    # percentual do corpo da barra de rompimento
    if kwargs["percentual_rompimento"]:
        res = dotenv.set_key(
            fconf, "PERCENTUAL_ROMPIMENTO", kwargs["percentual_rompimento"]
        )
    # fonte dos dados
    if kwargs["dados"]:
        res = dotenv.set_key(fconf, "DADOS", kwargs["dados"].upper())
    # caminho da pasta do MT5
    if kwargs["mt5_pasta"]:
        res = dotenv.set_key(fconf, "MT5_PASTA", kwargs["mt5_pasta"])
    if res:
        click.echo("%s=%s" % (res[1], res[2]))
        return

    # Verifica se o arquivo de configuração existe
    if not os.path.exists(fconf):
        # cria o arquivo e define as variáveis padrão
        for chave, valor in default.items():
            dotenv.set_key(fconf, chave.upper(), os.getenv(chave.upper(), valor))

    # Lista as variáveis disponíveis
    vars = dotenv.dotenv_values(fconf)
    for var in vars.items():
        click.echo("%s=%s" % (var[0], var[1]))


if __name__ == "__main__":
    conf()

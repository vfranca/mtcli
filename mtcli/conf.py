"""Gerencia configurações registradas no mtcli.ini."""

import os
import configparser
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


CONFIG_PATH = os.path.abspath("mtcli.ini")


def carregar_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_PATH):
        config.read(CONFIG_PATH)
    else:
        config["DEFAULT"] = {}
    return config


def salvar_config(config):
    with open(CONFIG_PATH, "w") as f:
        config.write(f)


@click.command()
@click.option("--list", "list_", is_flag=True, help="Lista todas as configurações.")
@click.option("--set", "set_", nargs=2, help="Define o valor de uma configuração.")
@click.option("--get", help="Exibe o valor de uma configuração.")
@click.option("--reset", is_flag=True, help="Redefine as configurações padrão.")
def conf(list_, set_, get, reset):
    """Gerencia configurações registradas no mtcli.ini."""
    config = carregar_config()

    if list_:
        for key in config["DEFAULT"]:
            click.echo(f"{key} = {config['DEFAULT'][key]}")

    elif set_:
        chave, valor = set_
        config["DEFAULT"][chave] = valor
        salvar_config(config)
        click.echo(f"Configuração '{chave}' definida como '{valor}'.")

    elif get:
        valor = config["DEFAULT"].get(get)
        if valor is not None:
            click.echo(f"{get} = {valor}")
        else:
            click.echo(f"Configuração '{get}' não encontrada.")

    elif reset:
        config["DEFAULT"].clear()
        salvar_config(config)
        click.echo("Configurações redefinidas.")

    else:
        click.echo(
            "Nenhuma opção fornecida. Use --help para ver as opções disponíveis."
        )

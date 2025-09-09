"""Gerencia configurações registradas no mtcli.ini."""

import os
import configparser
from configparser import MissingSectionHeaderError
import click
import MetaTrader5 as mt5
from mtcli.conecta import conectar, shutdown


CONFIG_PATH = os.path.abspath("mtcli.ini")


def carregar_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_PATH):
        try:
            config.read(CONFIG_PATH)
        except MissingSectionHeaderError as e:
            print(f"Erro: o arquivo '{CONFIG_PATH}' não contém seções válidas.")
            print("Certifique-se de que ele está no formato correto:")
            print("[padrao]\nCHAVE=valor")
            exit(1)
    else:
        config["DEFAULT"] = {}
    return config


def salvar_config(config):
    with open(CONFIG_PATH, "w") as f:
        config.write(f)


config = carregar_config()
section = "DEFAULT"
symbol = os.getenv("SYMBOL", config[section].get("symbol", fallback="WIN$N"))
digitos = int(os.getenv("DIGITOS", config[section].getint("digitos", fallback=2)))
period = os.getenv("PERIOD", config[section].get("period", fallback="D1"))
periodos = count = int(
    os.getenv("COUNT", config[section].getint("count", fallback=999))
)
view = os.getenv("VIEW", config[section].get("view", fallback="ch"))
volume = os.getenv("VOLUME", config[section].get("volume", fallback="tick"))
date = os.getenv("DATE", config[section].get("date", fallback=""))

lateral = os.getenv("LATERAL", config[section].get("lateral", fallback="doji"))
alta = os.getenv("ALTA", config[section].get("alta", fallback="verde"))
baixa = os.getenv("BAIXA", config[section].get("baixa", fallback="vermelho"))
rompimento_alta = os.getenv(
    "ROMPIMENTO_ALTA", config[section].get("rompimento_alta", fallback="c")
)
rompimento_baixa = os.getenv(
    "ROMPIMENTO_BAIXA", config[section].get("rompimento_baixa", fallback="v")
)
percentual_rompimento = int(
    os.getenv(
        "PERCENTUAL_ROMPIMENTO",
        config[section].getint("percentual_rompimento", fallback=50),
    )
)
percentual_doji = int(
    os.getenv("PERCENTUAL_DOJI", config[section].getint("percentual_doji", fallback=10))
)
up_bar = os.getenv("UP_BAR", config[section].get("up_bar", fallback="asc"))
down_bar = os.getenv("DOWN_BAR", config[section].get("down_bar", fallback="desc"))
inside_bar = os.getenv("INSIDE_BAR", config[section].get("inside_bar", fallback="ib"))
outside_bar = os.getenv(
    "OUTSIDE_BAR", config[section].get("outside_bar", fallback="ob")
)
sombra_superior = os.getenv(
    "SOMBRA_SUPERIOR", config[section].get("sombra_superior", fallback="top")
)
sombra_inferior = os.getenv(
    "SOMBRA_INFERIOR", config[section].get("sombra_inferior", fallback="bottom")
)
data_source = dados = os.getenv("DADOS", config[section].get("dados", fallback="mt5"))
csv_path = mt5_pasta = os.getenv(
    "MT5_PASTA", config[section].get("mt5_pasta", fallback="")
)


def get_data_source():
    from mtcli.data import CsvDataSource, MT5DataSource

    if data_source.lower() == "csv":
        return CsvDataSource()
    elif data_source.lower() == "mt5":
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

"""
Configurações principais do mtcli.

Este módulo centraliza a leitura de configurações provenientes de:

1. Variáveis de ambiente
2. Arquivo mtcli.ini

As variáveis de ambiente sempre têm prioridade sobre o arquivo INI.

Também fornece utilidades para obter o caminho de arquivos do
terminal MetaTrader5 e selecionar a fonte de dados (CSV ou MT5).

O acesso ao terminal MT5 é realizado apenas sob demanda para evitar
efeitos colaterais durante a importação do módulo (import side effects),
facilitando testes automatizados e execução em ambientes CI/CD.
"""

import os
import configparser

import MetaTrader5 as mt5

from mtcli.mt5_context import mt5_conexao

# ---------------------------------------------------------
# Carregamento do arquivo de configuração
# ---------------------------------------------------------

<<<<<<< HEAD
section = "DEFAULT"
SYMBOL = os.getenv("SYMBOL", config[section].get("symbol", fallback="WIN$N"))
DIGITOS = int(os.getenv("DIGITOS", config[section].getint("digitos", fallback=2)))
PERIOD = period = os.getenv("PERIOD", config[section].get("period", fallback="D1"))
PERIODOS = int(os.getenv("COUNT", config[section].getint("count", fallback=999)))
VIEW = view = os.getenv("VIEW", config[section].get("view", fallback="ch"))
VOLUME = volume = os.getenv("VOLUME", config[section].get("volume", fallback="tick"))
DATE = date = os.getenv("DATE", config[section].get("date", fallback=""))

DOJI = os.getenv("LATERAL", config[section].get("lateral", fallback="doji"))
BULL = os.getenv("BULL", config[section].get("bull", fallback="verde"))
BEAR = os.getenv("BEAR", config[section].get("bear", fallback="vermelho"))
BULLBREAKOUT = os.getenv(
    "BULLBREAKOUT", config[section].get("bullbreakout", fallback="c")
)
BEARBREAKOUT = os.getenv(
    "BEARBREAKOUT", config[section].get("bearbreakout", fallback="v")
)
PERCENTUAL_BREAKOUT = int(
    os.getenv(
        "PERCENTUAL_BREAKOUT",
        config[section].getint("percentual_breakout", fallback=50),
    )
)
PERCENTUAL_DOJI = int(
    os.getenv("PERCENTUAL_DOJI", config[section].getint("percentual_doji", fallback=10))
)
UPBAR = os.getenv("UPBAR", config[section].get("upbar", fallback="asc"))
DOWNBAR = os.getenv("DOWNBAR", config[section].get("downbar", fallback="desc"))
INSIDEBAR = os.getenv("INSIDEBAR", config[section].get("insidebar", fallback="ib"))
OUTSIDEBAR = os.getenv("OUTSIDEBAR", config[section].get("outsidebar", fallback="ob"))
TOPTAIL = os.getenv("TOPTAIL", config[section].get("toptail", fallback="top"))
BOTTOMTAIL = os.getenv(
    "BOTTOMTAIL", config[section].get("bottomtail", fallback="bottom")
)
data_source = dados = os.getenv("DADOS", config[section].get("dados", fallback="mt5"))
csv_path = mt5_pasta = os.getenv(
    "MT5_PASTA", config[section].get("mt5_pasta", fallback="")
)
=======
CONFIG_FILE = "mtcli.ini"
SECTION = "DEFAULT"

config = configparser.ConfigParser()
config.read(CONFIG_FILE)
>>>>>>> master


def get_config_value(key: str, cast=None, fallback=None):
    """
    Retorna um valor de configuração.

    A prioridade de leitura é:
    1. Variável de ambiente
    2. Arquivo mtcli.ini
    3. Valor fallback

    Args:
        key (str): Nome da chave de configuração.
        cast (type | None): Tipo de conversão (ex: int, float).
        fallback (Any): Valor padrão caso não encontrado.

    Returns:
        Any: valor convertido ou fallback.
    """
    value = os.getenv(key)

    if value is None:
        try:
            if cast == int:
                value = config.getint(SECTION, key, fallback=fallback)
            elif cast == float:
                value = config.getfloat(SECTION, key, fallback=fallback)
            else:
                value = config.get(SECTION, key, fallback=fallback)
        except (configparser.NoOptionError, ValueError):
            value = fallback
    else:
        if cast:
            try:
                value = cast(value)
            except ValueError:
                value = fallback

    return value


# ---------------------------------------------------------
# Configurações gerais
# ---------------------------------------------------------

SYMBOL = get_config_value("symbol", fallback="WIN$N")
DIGITOS = get_config_value("digitos", cast=int, fallback=2)
PERIOD = get_config_value("period", fallback="D1")
BARS = get_config_value("count", cast=int, fallback=999)

VIEW = get_config_value("view", fallback="ch")
VOLUME = get_config_value("volume", fallback="tick")
DATE = get_config_value("date", fallback="")

# ---------------------------------------------------------
# Configurações de leitura de candles
# ---------------------------------------------------------

LATERAL = get_config_value("lateral", fallback="doji")
ALTA = get_config_value("alta", fallback="verde")
BAIXA = get_config_value("baixa", fallback="vermelho")

ROMPIMENTO_ALTA = get_config_value("rompimento_alta", fallback="c")
ROMPIMENTO_BAIXA = get_config_value("rompimento_baixa", fallback="v")

PERCENTUAL_ROMPIMENTO = get_config_value(
    "percentual_rompimento", cast=int, fallback=50
)

PERCENTUAL_DOJI = get_config_value(
    "percentual_doji", cast=int, fallback=10
)

# ---------------------------------------------------------
# Configurações de padrões de barra
# ---------------------------------------------------------

UP_BAR = get_config_value("up_bar", fallback="asc")
DOWN_BAR = get_config_value("down_bar", fallback="desc")

INSIDE_BAR = get_config_value("inside_bar", fallback="ib")
OUTSIDE_BAR = get_config_value("outside_bar", fallback="ob")

SOMBRA_SUPERIOR = get_config_value("sombra_superior", fallback="top")
SOMBRA_INFERIOR = get_config_value("sombra_inferior", fallback="bottom")

# ---------------------------------------------------------
# Fonte de dados
# ---------------------------------------------------------

DATA_SOURCE = get_config_value("dados", fallback="mt5").lower()

# caminho inicial (pode vir do ini/env)
_INITIAL_CSV_PATH = get_config_value("mt5_pasta", fallback="")


def get_csv_path():
    """
    Retorna o caminho da pasta de arquivos do MT5 ou CSV.

    Se o caminho não estiver definido no mtcli.ini ou nas
    variáveis de ambiente, o terminal MT5 é consultado para
    descobrir automaticamente a pasta MQL5/Files.

    Returns:
        str: caminho normalizado da pasta de arquivos.
    """
    if _INITIAL_CSV_PATH:
        path = _INITIAL_CSV_PATH
    else:
        with mt5_conexao():
            terminal_info = mt5.terminal_info()

            if terminal_info is None:
                raise RuntimeError(
                    "Não foi possível obter as informações do terminal MT5."
                )

        path = os.path.join(terminal_info.data_path, "MQL5", "Files")

    return os.path.normpath(path) + os.sep


# ---------------------------------------------------------
# Factory de DataSource
# ---------------------------------------------------------

def get_data_source(source=None):
    """
    Retorna a fonte de dados configurada.

    Args:
        source (str | None): sobrescreve DATA_SOURCE se fornecido.

    Returns:
        CsvDataSource | MT5DataSource

    Raises:
        ValueError: se a fonte de dados não for reconhecida.
    """
    from mtcli.data import CsvDataSource, MT5DataSource

    src = source.lower() if source else DATA_SOURCE

    if src == "csv":
        return CsvDataSource()

    if src == "mt5":
        return MT5DataSource()

    raise ValueError(f"Fonte de dados desconhecida: {src}")


# ---------------------------------------------------------
# Timeframes suportados
# ---------------------------------------------------------

_HOURS = [12, 8, 6, 4, 3, 2, 1]
_MINUTES = [30, 20, 15, 12, 10, 6, 5, 4, 3, 2, 1]

TIMEFRAMES = (
    ["mn1", "w1", "d1"]
    + [f"h{i}" for i in _HOURS]
    + [f"m{i}" for i in _MINUTES]
)

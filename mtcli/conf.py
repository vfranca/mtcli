import os

import MetaTrader5 as mt5

from mtcli.conecta import conectar, shutdown
from mtcli.models.conf_model import ConfModel

config = ConfModel("mtcli.ini").carregar()

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

TIMEFRAMES = timeframes = [
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

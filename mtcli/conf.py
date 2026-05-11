"""
Sistema central de configuração do mtcli.
"""

import os
import configparser
import MetaTrader5 as mt5

from mtcli.mt5_context import mt5_conexao


class Config:
    def __init__(self, filename="mtcli.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(filename)

    def get(self, key, section="DEFAULT", cast=None, default=None):
        env_key = f"{section.upper()}_{key.upper()}"
        value = os.getenv(env_key) or os.getenv(key.upper())

        if value is None:
            if self.config.has_option(section, key):
                value = self.config.get(section, key)
            elif self.config.has_option("DEFAULT", key):
                value = self.config.get("DEFAULT", key)
            else:
                value = default

        if cast and value is not None:
            try:
                if cast is bool:
                    value = str(value).lower() in ("1", "true", "yes")
                else:
                    value = cast(value)
            except ValueError:
                value = default

        return value

    def section(self, section):
        class Section:
            def __init__(self, parent, section):
                self.parent = parent
                self.section = section

            def get(self, key, cast=None, default=None):
                return self.parent.get(key, self.section, cast, default)

        return Section(self, section)

    def get_csv_path(self):
        path = self.get("mt5_pasta")

        if path:
            return os.path.normpath(path) + os.sep

        with mt5_conexao():
            info = mt5.terminal_info()

            if info is None:
                raise RuntimeError(
                    "Não foi possível obter informações do terminal MT5."
                )

        path = os.path.join(info.data_path, "MQL5", "Files")
        return os.path.normpath(path) + os.sep


# instância global
conf = Config()

# compatibilidade retroativa
config = conf.config

# ----------------------------
# CONFIGURAÇÕES
# ----------------------------

DATA_SOURCE_NAME = conf.get("dados", default="mt5").lower()

SYMBOL = conf.get("symbol", default="WIN$N")
DIGITS = conf.get("digits", cast=int, default=0)
TIMEFRAME = conf.get("timeframe", default="M5")
MAX_BARS = conf.get("max_bars", cast=int, default=20)
VIEW = conf.get("view", default="hl")
VOLUME_TYPE = conf.get("volume", default="tick")
DATE = conf.get("date", default="")

PERCENTUAL_BREAKOUT = conf.get("percentual_breakout", cast=int, default=50)
PERCENTUAL_DOJI = conf.get("percentual_doji", cast=int, default=10)

_INITIAL_CSV_PATH = conf.get_csv_path()

# ----------------------------
# LABELS
# ----------------------------

DOJI = conf.get("lateral", default="doji")
UP = conf.get("up", default="verde")
DOWN = conf.get("down", default="vermelho")

ASCENDING = conf.get("ascending", default="asc")
DESCENDING = conf.get("descending", default="desc")
INTERNAL = conf.get("internal", default="int")
EXTERNAL = conf.get("external", default="ext")
UNKNOW = conf.get("unknow", default="unk")

UPPER_WICK = conf.get("upper_wick", default="upper")
LOWER_WICK = conf.get("lower_wick", default="lower")

# ----------------------------
# PROCESSOS
# ----------------------------

RUN_DIR = os.path.join(
    os.getenv("APPDATA", os.path.expanduser("~")),
    "mtcli",
    "run"
)

os.makedirs(RUN_DIR, exist_ok=True)

PID_FILE = os.path.join(RUN_DIR, "risco.pid")
STOP_FILE = os.path.join(RUN_DIR, "risco.stop")
HEARTBEAT_FILE = os.path.join(RUN_DIR, "risco.heartbeat")

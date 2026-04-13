"""
Sistema central de configuração do mtcli.

Fornece leitura de configuração a partir de:

1. Variáveis de ambiente
2. Arquivo mtcli.ini
3. Valores default

Também oferece utilidades usadas por plugins como:

- descoberta do diretório MQL5/Files
- seleção da fonte de dados (CSV ou MT5)

Plugins novos devem acessar a configuração através do objeto global `conf`.

Compatibilidade retroativa:
---------------------------
Plugins antigos utilizavam:

    from mtcli.conf import config

onde `config` era um objeto `configparser.ConfigParser`.

Para manter compatibilidade com plugins já publicados,
o objeto `config` continua sendo exposto.

Essa API é considerada **deprecated** e poderá ser removida
em versões futuras do mtcli.
"""

import os
import configparser

import MetaTrader5 as mt5

from mtcli.mt5_context import mt5_conexao


class Config:
    """
    Gerenciador central de configurações do mtcli.

    Permite acessar valores a partir de:

    - variáveis de ambiente
    - arquivo mtcli.ini
    - valores default

    Plugins devem preferencialmente usar:

        from mtcli.conf import conf
        conf.get(...)
    """

    def __init__(self, filename="mtcli.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(filename)

    # ---------------------------------------------------------
    # leitura de valores
    # ---------------------------------------------------------

    def get(self, key, section="DEFAULT", cast=None, default=None):
        """
        Retorna um valor de configuração.

        Prioridade:

        1. Variável de ambiente SECTION_KEY
        2. Variável de ambiente KEY
        3. mtcli.ini [section]
        4. mtcli.ini [DEFAULT]
        5. default

        Args:
            key (str):
                Nome da configuração.

            section (str):
                Seção do arquivo mtcli.ini.

            cast (type | None):
                Tipo para conversão do valor.

            default (Any):
                Valor padrão.

        Returns:
            Any
        """

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

    # ---------------------------------------------------------
    # seção helper
    # ---------------------------------------------------------

    def section(self, section):
        """
        Retorna um helper para acessar uma seção específica.

        Example:

            renko = conf.section("renko")
            brick = renko.get("brick", cast=int, default=10)
        """

        class Section:
            def __init__(self, parent, section):
                self.parent = parent
                self.section = section

            def get(self, key, cast=None, default=None):
                return self.parent.get(key, self.section, cast, default)

        return Section(self, section)

    # ---------------------------------------------------------
    # caminho MT5
    # ---------------------------------------------------------

    def get_csv_path(self):
        """
        Retorna o caminho da pasta MQL5/Files do MetaTrader 5.

        A prioridade é:

        1. mtcli.ini -> mt5_pasta
        2. descoberta automática via MT5

        Returns:
            str: caminho normalizado da pasta Files.
        """

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

    # ---------------------------------------------------------
    # data source
    # ---------------------------------------------------------

    def get_data_source(self, source=None):
        """
        Retorna a fonte de dados configurada.

        Args:
            source (str | None):
                Fonte explícita ("csv" ou "mt5").

        Returns:
            DataSource
        """

        from mtcli.data import CsvDataSource, MT5DataSource

        src = (source or self.get("dados", default="mt5")).lower()

        if src == "csv":
            return CsvDataSource()

        if src == "mt5":
            return MT5DataSource()

        raise ValueError(f"Fonte de dados desconhecida: {src}")


# ---------------------------------------------------------
# instância global usada por todo o sistema
# ---------------------------------------------------------

conf = Config()

# ---------------------------------------------------------
# compatibilidade com plugins antigos
# ---------------------------------------------------------
#
# Plugins antigos utilizam:
#
#     from mtcli.conf import config
#
# onde `config` era um ConfigParser.
#
# Mantemos esse objeto apontando para o ConfigParser interno
# para evitar quebra de compatibilidade.
#
# API DEPRECATED – usar `conf.get()` em novos plugins.
#

config = conf.config


# ---------------------------------------------------------
# timeframes suportados
# ---------------------------------------------------------

_HOURS = [12, 8, 6, 4, 3, 2, 1]
_MINUTES = [30, 20, 15, 12, 10, 6, 5, 4, 3, 2, 1]

TIMEFRAMES = (
    ["mn1", "w1", "d1"]
    + [f"h{i}" for i in _HOURS]
    + [f"m{i}" for i in _MINUTES]
)

# ---------------------------------------------------------
# Configurações gerais
# ---------------------------------------------------------

SYMBOL = conf.get("symbol", default="WIN$N")
DIGITOS = conf.get("digitos", cast=int, default=2)
PERIOD = conf.get("period", default="D1")
BARS = conf.get("count", cast=int, default=999)

VIEW = conf.get("view", default="ch")
VOLUME = conf.get("volume", default="tick")
DATE = conf.get("date", default="")

# ---------------------------------------------------------
# Configurações de leitura de candles
# ---------------------------------------------------------

DOJI = conf.get("lateral", default="doji")
BULL = conf.get("bull", default="verde")
BEAR = conf.get("bear", default="vermelho")

BULLBREAKOUT = conf.get("bullbreakout", default="c")
BEARBREAKOUT = conf.get("bearbreakout", default="v")

PERCENTUAL_BREAKOUT = conf.get(
    "percentual_breakout",
    cast=int,
    default=50,
)

PERCENTUAL_DOJI = conf.get(
    "percentual_doji",
    cast=int,
    default=10,
)

# ---------------------------------------------------------
# Configurações de padrões de barra
# ---------------------------------------------------------

UPBAR = conf.get("upbar", default="asc")
DOWNBAR = conf.get("downbar", default="desc")
INSIDEBAR = conf.get("insidebar", default="ib")
OUTSIDEBAR = conf.get("outsidebar", default="ob")

TOPTAIL = conf.get("toptail", default="top")
BOTTOMTAIL = conf.get("bottomtail", default="bottom")

# ---------------------------------------------------------
# Fonte de dados
# ---------------------------------------------------------

DATA_SOURCE_NAME = conf.get("dados", default="mt5").lower()
DATA_SOURCE = conf.get_data_source()

# ---------------------------------------------------------
# caminho inicial do CSV (pode vir do ini/env)
# ---------------------------------------------------------

_INITIAL_CSV_PATH = conf.get_csv_path()

# ---------------------------------------------------------
# Gestão de processos (daemon / serviços mtcli)
# ---------------------------------------------------------
#
# Define caminhos para arquivos de controle utilizados por
# processos em background (ex: ticks, risco, etc.).
#
# Conceitos:
#
# PID FILE
#     Armazena o PID do processo ativo.
#     Usado para garantir instância única e controle externo.
#
# STOP FILE
#     Arquivo sentinela para sinalizar encerramento gracioso.
#     O processo monitora sua existência periodicamente.
#
# HEARTBEAT FILE
#     Atualizado continuamente pelo processo.
#     Permite verificar se o serviço está vivo ou travado.
#
# Diretório base:
#     %APPDATA%/mtcli/run (Windows)
#     ~/.mtcli/run        (fallback)
#
# Cada serviço define seus próprios arquivos (ex: ticks, risco).
#
# Exemplo:
#     ticks.pid
#     ticks.stop
#     ticks.heartbeat
#

RUN_DIR = os.path.join(
    os.getenv("APPDATA", os.path.expanduser("~")),
    "mtcli",
    "run"
)

os.makedirs(RUN_DIR, exist_ok=True)

PID_FILE = os.path.join(RUN_DIR, "risco.pid")
STOP_FILE = os.path.join(RUN_DIR, "risco.stop")
HEARTBEAT_FILE = os.path.join(RUN_DIR, "risco.heartbeat")

"""
Sistema central de logging do mtcli.

Este módulo fornece uma função única `setup_logger()` utilizada por todo
o ecossistema de plugins do mtcli para configurar logging consistente.

Características principais
--------------------------

* Arquivo de log rotativo em:
  %APPDATA%/mtcli/logs/

* Rotação automática:
  - tamanho máximo: 2 MB
  - até 3 arquivos de backup

* Proteção contra duplicação de handlers quando plugins
  inicializam o logger múltiplas vezes.

* Encoding UTF-8 garantido (evita problemas de acentuação
  no Windows).

* Compatível com pytest (caplog).

* Suporte opcional a logs por processo (multi-process safe)

Variáveis de ambiente
---------------------

MTCLI_LOG_PER_PROCESS=1
    cria arquivos separados por PID
    exemplo: mtcli-1234.log

MTCLI_LOG_NAME=risco
    define nome base do arquivo de log

Observação
----------

Os logs **não são exibidos no console**.
Toda saída é direcionada exclusivamente para arquivo.
"""

import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path


# ==========================================================
# DIRETÓRIO DE LOG
# ==========================================================

base_dir = os.getenv("APPDATA", os.path.expanduser("~"))

LOG_DIR = Path(base_dir) / "mtcli" / "logs"

LOG_DIR.mkdir(parents=True, exist_ok=True)


# ==========================================================
# RESOLUÇÃO DO NOME DO LOG
# ==========================================================

def _resolve_log_file() -> Path:
    """
    Resolve dinamicamente o caminho do arquivo de log.

    Mantém compatibilidade com versões anteriores
    mas permite novos modos via variáveis de ambiente.
    """

    log_name = os.getenv("MTCLI_LOG_NAME", "mtcli")

    per_process = os.getenv("MTCLI_LOG_PER_PROCESS")

    if per_process:
        pid = os.getpid()
        filename = f"{log_name}-{pid}.log"
    else:
        filename = f"{log_name}.log"

    return LOG_DIR / filename


LOG_FILE = _resolve_log_file()


# ==========================================================
# LOGGER SETUP
# ==========================================================

def setup_logger(name: str = "mtcli") -> logging.Logger:
    """
    Cria ou retorna um logger configurado para o mtcli.

    O logger utiliza **apenas um handler de arquivo rotativo**.
    Nenhuma saída é enviada ao console.

    A função é **idempotente**, ou seja, pode ser chamada
    múltiplas vezes sem duplicar handlers.

    Parameters
    ----------
    name : str
        Nome do logger (normalmente `__name__`).

    Returns
    -------
    logging.Logger
        Instância configurada do logger.
    """

    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # ======================================================
    # REMOVE STREAM HANDLERS (silencia console)
    # ======================================================

    for handler in list(logger.handlers):

        if isinstance(handler, logging.StreamHandler) and not isinstance(
            handler, RotatingFileHandler
        ):
            logger.removeHandler(handler)

    # ======================================================
    # EVITA DUPLICAÇÃO DE FILE HANDLER
    # ======================================================

    for handler in logger.handlers:

        if isinstance(handler, RotatingFileHandler):

            try:
                if Path(handler.baseFilename) == LOG_FILE:
                    return logger
            except Exception:
                pass

    # ======================================================
    # FILE HANDLER ROTATIVO
    # ======================================================

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=2_000_000,
        backupCount=3,
        encoding="utf-8",
        delay=True,
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    # ======================================================
    # PROPAGATION
    # ======================================================

    # Permite que pytest caplog capture logs
    logger.propagate = True

    return logger


# ==========================================================
# LOGGER PADRÃO DO MTCLI
# ==========================================================

log = setup_logger()

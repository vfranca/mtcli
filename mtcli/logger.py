"""
Sistema central de logging do mtcli.

Este módulo fornece uma função única `setup_logger()` utilizada por todo
o ecossistema de plugins do mtcli para configurar logging consistente.

Características principais
--------------------------

 Arquivo de log rotativo em:
  %APPDATA%/mtcli/logs/mtcli.log

 Rotação automática:
  - tamanho máximo: 2 MB
  - até 3 arquivos de backup

 Saída simultânea para:
  - arquivo
  - console (stdout)

 Compatível com pytest (caplog)

 Proteção contra duplicação de handlers quando plugins
  inicializam o logger múltiplas vezes.

 Encoding UTF-8 garantido (evita problemas de acentuação
  no Windows).

Uso típico
----------

    from mtcli.logger import setup_logger

    log = setup_logger(__name__)

    log.info("Mensagem de log")

Plugins devem sempre usar `setup_logger(__name__)`
para manter consistência nos logs.
"""

import logging
from logging.handlers import RotatingFileHandler
import os


# ==========================================================
# DIRETÓRIO DE LOG
# ==========================================================

base_dir = os.getenv("APPDATA", os.path.expanduser("~"))

LOG_DIR = os.path.join(base_dir, "mtcli", "logs")

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "mtcli.log")


# ==========================================================
# LOGGER SETUP
# ==========================================================

def setup_logger(name: str = "mtcli") -> logging.Logger:
    """
    Cria ou retorna um logger configurado para o mtcli.

    Este logger utiliza dois handlers:

    1️⃣ RotatingFileHandler
        Grava logs em arquivo com rotação automática.

    2️⃣ StreamHandler
        Exibe logs no console.

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

    # nível global
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # ======================================================
    # FILE HANDLER (ROTATING)
    # ======================================================

    file_handler_exists = any(
        isinstance(h, RotatingFileHandler) for h in logger.handlers
    )

    if not file_handler_exists:

        file_handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=2_000_000,
            backupCount=3,
            encoding="utf-8",  # evita problema de acentuação no Windows
            delay=True,        # abre o arquivo apenas quando necessário
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    # ======================================================
    # CONSOLE HANDLER
    # ======================================================

    console_handler_exists = any(
        isinstance(h, logging.StreamHandler) and not isinstance(h, RotatingFileHandler)
        for h in logger.handlers
    )

    if not console_handler_exists:

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    # ======================================================
    # PROPAGATION
    # ======================================================

    # Permite que pytest caplog capture logs
    logger.propagate = True

    return logger


# ==========================================================
# LOGGER PADRÃO DO MTCLI
# ==========================================================

"""
Logger padrão utilizado por módulos internos do mtcli.

Plugins geralmente criam seu próprio logger usando:

    setup_logger(__name__)
"""

log = setup_logger()

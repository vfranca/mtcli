"""
Sistema central de logging do mtcli.

Este módulo fornece uma função única `setup_logger()` utilizada por todo
o ecossistema de plugins do mtcli para configurar logging consistente.

Características principais
--------------------------

✔ Arquivo de log rotativo em:
  %APPDATA%/mtcli/logs/mtcli.log

✔ Rotação automática:
  - tamanho máximo: 2 MB
  - até 3 arquivos de backup

✔ Proteção contra duplicação de handlers quando plugins
  inicializam o logger múltiplas vezes.

✔ Encoding UTF-8 garantido (evita problemas de acentuação
  no Windows).

✔ Compatível com pytest (caplog).

Observação
----------

Os logs **não são exibidos no console**.
Toda saída é direcionada exclusivamente para o arquivo de log.
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
    # REMOVE STREAM HANDLERS (garante silêncio no console)
    # ======================================================

    for handler in list(logger.handlers):
        if isinstance(handler, logging.StreamHandler) and not isinstance(handler, RotatingFileHandler):
            logger.removeHandler(handler)

    # ======================================================
    # FILE HANDLER ROTATIVO
    # ======================================================

    file_handler_exists = any(
        isinstance(h, RotatingFileHandler) for h in logger.handlers
    )

    if not file_handler_exists:

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

"""
Logger padrão utilizado por módulos internos do mtcli.

Plugins geralmente criam seu próprio logger usando:

    setup_logger(__name__)
"""

log = setup_logger()

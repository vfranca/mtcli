"""
Sistema central de logging do mtcli.

Versão corrigida para evitar duplicação de logs em cenários com:

- múltiplos plugins
- múltiplos loggers
- integração com pytest (caplog)
- uso de logging básico por libs externas

Estratégia adotada
------------------

- Um único handler é configurado no ROOT logger
- Todos os loggers filhos propagam para o root
- Nenhum handler é anexado diretamente aos loggers de módulo

Isso elimina completamente duplicação de logs.

API permanece 100% compatível.
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
# RESOLUÇÃO DO ARQUIVO
# ==========================================================

def _resolve_log_file() -> Path:
    log_name = os.getenv("MTCLI_LOG_NAME", "mtcli")
    per_process = os.getenv("MTCLI_LOG_PER_PROCESS")

    if per_process:
        return LOG_DIR / f"{log_name}-{os.getpid()}.log"

    return LOG_DIR / f"{log_name}.log"


LOG_FILE = _resolve_log_file()


# ==========================================================
# CONTROLE GLOBAL (ANTI DUPLICAÇÃO)
# ==========================================================

_MTCLI_LOGGER_CONFIGURED = False


# ==========================================================
# SETUP
# ==========================================================

def setup_logger(name: str = "mtcli") -> logging.Logger:
    """
    Retorna logger configurado.

    A configuração real ocorre apenas uma vez no ROOT logger.

    Parameters
    ----------
    name : str
        Nome do logger.

    Returns
    -------
    logging.Logger
    """

    global _MTCLI_LOGGER_CONFIGURED

    root = logging.getLogger()

    # ------------------------------------------------------
    # CONFIGURAÇÃO GLOBAL (executa uma única vez)
    # ------------------------------------------------------

    if not _MTCLI_LOGGER_CONFIGURED:

        root.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # remove handlers existentes (evita duplicação externa)
        for h in list(root.handlers):
            root.removeHandler(h)

        file_handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=2_000_000,
            backupCount=3,
            encoding="utf-8",
            delay=True,
        )

        file_handler.setFormatter(formatter)

        root.addHandler(file_handler)

        _MTCLI_LOGGER_CONFIGURED = True

    # ------------------------------------------------------
    # LOGGER FILHO (sem handler próprio)
    # ------------------------------------------------------

    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    # 🔥 CRÍTICO: não anexar handler aqui
    logger.propagate = True

    return logger


# ==========================================================
# LOGGER PADRÃO
# ==========================================================

log = setup_logger()

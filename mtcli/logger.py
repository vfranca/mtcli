import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = os.path.join(os.path.expanduser("~"), ".mtcli")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "mtcli.log")


def setup_logger(name: str = "mtcli") -> logging.Logger:
    """Configura logger rotativo com saída em arquivo e console.

    - Escreve logs em ~/.mtcli/mtcli.log (máx. 2 MB, 3 backups).
    - Mostra logs também no console (stdout), capturáveis via pytest/caplog.
    - Evita duplicar handlers.
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # === File handler rotativo ===
    if not any(isinstance(h, RotatingFileHandler) for h in logger.handlers):
        file_handler = RotatingFileHandler(LOG_FILE, maxBytes=2_000_000, backupCount=3)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # === Stream handler (console) ===
    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # Permite que pytest caplog capture logs
    logger.propagate = True

    return logger


# Inicializa logger padrão
log = setup_logger()

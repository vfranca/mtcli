"""Módulo de logging."""

import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logger(name="mtcli"):
    if os.name == "nt":
        base_dir = os.getenv("APPDATA", os.path.expanduser("~"))
        log_dir = os.path.join(base_dir, name, "logs")
    else:
        base_dir = os.path.expanduser("~/.local/share")
        log_dir = os.path.join(base_dir, name, "logs")

    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f"{name}.log")

    handler = RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=3)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        logger.addHandler(handler)
    logger.propagate = False

    return logger

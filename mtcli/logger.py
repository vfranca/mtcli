"""Módulo  de logging."""

import logging
from datetime import datetime
import os


def setup_logger(nome="mtcli", log_dir="logs"):
    os.makedirs(log_dir, exist_ok=True)
    data = datetime.now().strftime("%Y-%m-%d")
    caminho = os.path.join(log_dir, f"{nome}_{data}.log")

    logger = logging.getLogger(nome)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(caminho, encoding="utf-8")
        fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    return logger

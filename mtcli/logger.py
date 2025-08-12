"""Módulo de logging."""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("mtcli.log"),  # Log em arquivo
        #         logging.StreamHandler()                   # Log no console
    ],
)
logger = logging.getLogger(__name__)

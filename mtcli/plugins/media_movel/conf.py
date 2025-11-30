import os

from mtcli.conf import config

PERIOD = os.getenv("PERIOD", config["DEFAULT"].get("period", fallback="M5"))
LIMIT = int(os.getenv("LIMIT", config["DEFAULT"].getint("limit", fallback=20)))
TIPO_MM = os.getenv("TIPO_MM", config["DEFAULT"].get("tipo_mm", fallback="sma"))
LINHAS = int(os.getenv("LINHAS", config["DEFAULT"].get("linhas", fallback=5)))
DIGITOS = int(os.getenv("DIGITOS", config["DEFAULT"].getint("digitos", fallback=0)))

"""
Configurações do plugin mm

Este módulo centraliza o carregamento das configurações utilizadas pelo
plugin MM a partir do arquivo de configuração do mtcli (mtcli.ini).

As configurações são lidas através do sistema:

    from mtcli.conf import conf

Seção utilizada:

    [mm]

Caso não exista configuração do usuário, valores padrão seguros são aplicados.

Exemplo de configuração:

    [mm]
    symbol = WIN$N
    digitos = 0
    timeframe = m1
    bars = 50
"""

from mtcli.conf import conf


# ==========================================================
# SEÇÃO DE CONFIGURAÇÃO
# ==========================================================

cfg = conf.section("mm")


# ==========================================================
# SÍMBOLO
# ==========================================================

SYMBOL = cfg.get("symbol", default="WIN$N")


# ==========================================================
# FORMATAÇÃO DE PREÇO
# ==========================================================

DIGITOS = cfg.get("digitos", cast=int, default=0)

if DIGITOS < 0:
    DIGITOS = 0


# ==========================================================
# TIMEFRAME
# ==========================================================

TIMEFRAME = cfg.get("timeframe", default="m1").lower()


# ==========================================================
# QUANTIDADE DE CANDLES
# ==========================================================

BARS = cfg.get("bars", cast=int, default=50)

if BARS <= 0:
    BARS = 50

TIPO_MM = cfg.get("tipo_mm", default="ema")

LIMIT = cfg.get("limit", cast=int, default=20)

LINHAS = cfg.get("linhas", cast=int, default=5)

PERIOD = cfg.get("period", default="m5")

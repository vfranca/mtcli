"""
Configurações do plugin vm

Este módulo centraliza o carregamento das configurações utilizadas pelo
plugin VM a partir do arquivo de configuração do mtcli (mtcli.ini).

As configurações são lidas através do sistema:

    from mtcli.conf import conf

Seção utilizada:

    [vm]

Caso não exista configuração do usuário, valores padrão seguros são aplicados.

Exemplo de configuração:

    [vm]
    symbol = WIN$N
    digitos = 0
    timeframe = m1
    bars = 50
"""

from mtcli.conf import conf


# ==========================================================
# SEÇÃO DE CONFIGURAÇÃO
# ==========================================================

cfg = conf.section("vm")


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

"""
Utilitários de conversão de tempo para o mtcli.

Este módulo fornece funções para:
- Obter o horário atual em UTC
- Converter datas de UTC para o timezone da B3 (Brasil)
- Converter datas da B3 para UTC

Todas as funções trabalham com objetos datetime timezone-aware.
"""

from datetime import datetime
from zoneinfo import ZoneInfo


# Timezones padrão
UTC = ZoneInfo("UTC")
B3_TZ = ZoneInfo("America/Sao_Paulo")


def now_utc():
    """
    Retorna o horário atual em UTC.

    Returns:
        datetime: Data/hora atual com timezone UTC (aware).
    """
    return datetime.now(tz=UTC)


def utc_to_b3(dt):
    """
    Converte um datetime em UTC para o timezone da B3.

    Caso o datetime seja naive (sem timezone), assume-se que ele já está em UTC.

    Args:
        dt (datetime): Data/hora em UTC (aware ou naive).

    Returns:
        datetime: Data/hora convertida para o timezone da B3.
    """
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=UTC)

    return dt.astimezone(B3_TZ)


def b3_to_utc(dt):
    """
    Converte um datetime do timezone da B3 para UTC.

    Caso o datetime seja naive (sem timezone), assume-se que ele já está
    no horário da B3 (America/Sao_Paulo).

    Args:
        dt (datetime): Data/hora no timezone da B3 (aware ou naive).

    Returns:
        datetime: Data/hora convertida para UTC.
    """
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=B3_TZ)

    return dt.astimezone(UTC)

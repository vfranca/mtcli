# mtcli/models/rate.py

from dataclasses import dataclass
from datetime import datetime
from typing import Any


def _parse_timestamp(value: Any) -> datetime:
    """
    Converte timestamp vindo da fonte de dados para datetime.

    Suporta:
    - datetime (pass-through)
    - 'YYYY.MM.DD HH:MM:SS' (formato padrão MT5)
    - ISO-8601 ('YYYY-MM-DD HH:MM:SS')
    """
    if isinstance(value, datetime):
        return value

    if isinstance(value, str):
        try:
            # MT5 padrão: 2026.01.30 18:07:00
            return datetime.strptime(value, "%Y.%m.%d %H:%M:%S")
        except ValueError:
            # Fallback ISO
            return datetime.fromisoformat(value)

    raise TypeError(f"Formato de timestamp não suportado: {value!r}")


@dataclass(frozen=True)
class RateDTO:
    """
    DTO de cotação bruta (OHLCV).

    Representa exatamente uma linha retornada pela fonte de dados
    (MT5, CSV, replay, etc), sem lógica de negócio.
    """

    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    tick_volume: int | None = None
    real_volume: int | None = None

    @classmethod
    def from_list(cls, rate: list) -> "RateDTO":
        """
        Cria um RateDTO a partir de uma lista no formato padrão mtcli.

        Args:
            rate (list):
                [datetime_str, open, high, low, close, tick_volume, real_volume]
        """
        return cls(
            timestamp=_parse_timestamp(rate[0]),
            open=float(rate[1]),
            high=float(rate[2]),
            low=float(rate[3]),
            close=float(rate[4]),
            tick_volume=int(rate[5]) if len(rate) > 5 and rate[5] is not None else None,
            real_volume=int(rate[6]) if len(rate) > 6 and rate[6] is not None else None,
        )

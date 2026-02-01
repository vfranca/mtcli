# mtcli/models/bars.py

from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, List

from mtcli.models.rate import RateDTO


@dataclass(frozen=True)
class BarModel:
    """
    Representa uma barra consolidada de preço (OHLCV).
    """

    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    tick_volume: int | None = None
    real_volume: int | None = None

    # ------------------------------------------------------------------
    # Direção
    # ------------------------------------------------------------------

    @property
    def is_bullish(self) -> bool:
        """Barra de alta."""
        return self.close >= self.open

    @property
    def is_bearish(self) -> bool:
        """Barra de baixa."""
        return self.close < self.open

    # ------------------------------------------------------------------
    # Medidas
    # ------------------------------------------------------------------

    @property
    def range(self) -> float:
        """Amplitude total da barra (high - low)."""
        return self.high - self.low

    @property
    def body(self) -> float:
        """Tamanho do corpo da barra."""
        return abs(self.close - self.open)

    @property
    def upper_wick(self) -> float:
        """Pavio superior."""
        return self.high - max(self.open, self.close)

    @property
    def lower_wick(self) -> float:
        """Pavio inferior."""
        return min(self.open, self.close) - self.low


class BarsModel:
    """
    Builder de barras a partir de RateDTO.
    """

    def __init__(
        self,
        rates: Iterable[RateDTO],
        date_filter: str | None = None,
    ):
        self.rates = list(rates)
        self.date_filter = date_filter

    def build(self) -> List[BarModel]:
        bars: List[BarModel] = []

        for r in self.rates:
            if self.date_filter:
                if r.timestamp.date().isoformat() != self.date_filter:
                    continue

            bars.append(
                BarModel(
                    timestamp=r.timestamp,
                    open=r.open,
                    high=r.high,
                    low=r.low,
                    close=r.close,
                    tick_volume=r.tick_volume,
                    real_volume=r.real_volume,
                )
            )

        return bars

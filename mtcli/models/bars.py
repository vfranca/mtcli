# mtcli/models/bars.py

from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, List

from mtcli.models.rate import RateDTO


@dataclass(frozen=True)
class BarModel:
    """
    Representa uma barra consolidada de preço (OHLCV),
    incluindo sua relação estrutural com o candle anterior.
    """

    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    tick_volume: int | None = None
    real_volume: int | None = None
    previous: "BarModel | None" = None

    # ------------------------------------------------------------------
    # Direção simples
    # ------------------------------------------------------------------

    @property
    def is_bullish(self) -> bool:
        return self.close >= self.open

    @property
    def is_bearish(self) -> bool:
        return self.close < self.open

    # ------------------------------------------------------------------
    # Medidas
    # ------------------------------------------------------------------

    @property
    def range(self) -> float:
        return self.high - self.low

    @property
    def body(self) -> float:
        return abs(self.close - self.open)

    @property
    def upper_wick(self) -> float:
        return self.high - max(self.open, self.close)

    @property
    def lower_wick(self) -> float:
        return min(self.open, self.close) - self.low

    # ------------------------------------------------------------------
    # Estrutura em relação ao candle anterior
    # ------------------------------------------------------------------

    @property
    def is_ascending(self) -> bool:
        if not self.previous:
            return False
        return (
            self.high > self.previous.high
            and self.low > self.previous.low
        )

    @property
    def is_descending(self) -> bool:
        if not self.previous:
            return False
        return (
            self.high < self.previous.high
            and self.low < self.previous.low
        )

    @property
    def is_external(self) -> bool:
        if not self.previous:
            return False
        return (
            self.high > self.previous.high
            and self.low < self.previous.low
        )

    @property
    def is_internal(self) -> bool:
        if not self.previous:
            return False
        return (
            self.high < self.previous.high
            and self.low > self.previous.low
        )

    @property
    def structure(self) -> str:
        """
        Retorna:
        - ASC  → barra ascendente
        - DESC → barra descendente
        - EXT  → barra externa
        - INT  → barra interna
        - N/A  → primeira barra
        """
        if not self.previous:
            return "N/A"
        if self.is_external:
            return "EXT"
        if self.is_internal:
            return "INT"
        if self.is_ascending:
            return "ASC"
        if self.is_descending:
            return "DESC"
        return "N/A"

    @property
    def structure_symbol(self) -> str:
        """
        Símbolo visual da estrutura.
        """
        return {
            "ASC": "↑",
            "DESC": "↓",
            "EXT": "↕",
            "INT": "▢",
            "N/A": "·",
        }[self.structure]


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
        previous: BarModel | None = None

        for r in self.rates:
            if self.date_filter:
                if r.timestamp.date().isoformat() != self.date_filter:
                    continue

            bar = BarModel(
                timestamp=r.timestamp,
                open=r.open,
                high=r.high,
                low=r.low,
                close=r.close,
                tick_volume=r.tick_volume,
                real_volume=r.real_volume,
                previous=previous,
            )

            bars.append(bar)
            previous = bar

        return bars

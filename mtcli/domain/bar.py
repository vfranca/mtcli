from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Bar:
    """
    Representa um candle OHLCV independente de fonte de dados.

    - tick_volume: quantidade de ticks (atividade)
    - real_volume: volume negociado (quando disponível)
    """

    time: datetime
    open: float
    high: float
    low: float
    close: float
    tick_volume: float
    real_volume: float | None = None

    def is_bull(self) -> bool:
        return self.close > self.open

    def is_bear(self) -> bool:
        return self.close < self.open

    def body(self) -> float:
        return abs(self.close - self.open)

    def range(self) -> float:
        return self.high - self.low

    def volume(self) -> float:
        """
        Volume preferencial:
        - usa real_volume se disponível
        - fallback para tick_volume
        """
        return self.real_volume or self.tick_volume

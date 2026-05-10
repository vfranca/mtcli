from dataclasses import dataclass


@dataclass(frozen=True)
class Tick:
    time: datetime
    bid: float
    ask: float
    volume: float

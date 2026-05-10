from dataclasses import dataclass


@dataclass(frozen=True)
class Symbol:
    name: str
    digits: int
    point: float
    tick_size: float
    tick_value: float

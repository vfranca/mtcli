@dataclass(frozen=True)
class TradingConfig:
    risk_per_trade: float
    max_positions: int

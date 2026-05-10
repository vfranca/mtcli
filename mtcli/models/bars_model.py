"""
Modelos de barras (OHLCV) e construção de estrutura.

Responsável por:
- transformar RateDTO em BarModel
- definir relações estruturais entre candles
- fornecer métricas úteis para análise de price action

Este módulo concentra a lógica de domínio (core trading).
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, List

from .rate_model import RateDTO


@dataclass(frozen=True)
class BarModel:
    """
    Representa uma barra OHLCV enriquecida com contexto estrutural.

    Atributos:
        previous: referência para barra anterior (encadeamento)
    """

    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    tick_volume: int | None = None
    real_volume: int | None = None
    previous: "BarModel | None" = None

    @property
    def is_bullish(self) -> bool:
        return self.close >= self.open

    @property
    def is_bearish(self) -> bool:
        return self.close < self.open

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

    # ---------------- Estrutura ---------------- #

    @property
    def is_ascending(self) -> bool:
        return (
            self.previous
            and self.high > self.previous.high
            and self.low > self.previous.low
        )

    @property
    def is_descending(self) -> bool:
        return (
            self.previous
            and self.high < self.previous.high
            and self.low < self.previous.low
        )

    @property
    def is_external(self) -> bool:
        return (
            self.previous
            and self.high > self.previous.high
            and self.low < self.previous.low
        )

    @property
    def is_internal(self) -> bool:
        return (
            self.previous
            and self.high < self.previous.high
            and self.low > self.previous.low
        )

    @property
    def structure(self) -> str:
        """
        Classificação estrutural da barra.

        Retornos:
            ASC  → tendência de alta
            DESC → tendência de baixa
            EXT  → expansão (range maior)
            INT  → contração (inside bar)
            N/A  → primeira barra ou indefinido
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
        Alias visual da estrutura (mantido para compatibilidade de views).
        """
        return {
            "ASC": "ASC",
            "DESC": "DESC",
            "EXT": "EXT",
            "INT": "INT",
            "N/A": "UNK",
        }[self.structure]


class BarsModel:
    """
    Constrói uma sequência de BarModel a partir de RateDTO.

    Aplica:
    - filtro de data (pregão)
    - encadeamento entre barras (previous)
    """

    def __init__(
        self,
        rates: Iterable[RateDTO],
        date_filter: str | None = None,
    ):
        self.rates = list(rates)
        self.date_filter = date_filter

    def build(self) -> List[BarModel]:
        """
        Constrói a lista de barras encadeadas.

        Returns:
            List[BarModel]
        """
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

from mtcli.models.bar import BarModel


class ChartModel:
    """
        Modelo de apoio para cálculo de estatísticas do gráfico.
    """

    def __init__(self, bars: list[BarModel]):
        self.bars = bars

    def high(self) -> float:
        """Máxima do período."""
        return max(bar.high for bar in self.bars)

    def low(self) -> float:
        """Mínima do período."""
        return min(bar.low for bar in self.bars)

    def vwap(self) -> float:
        """VWAP simples do período."""
        total_vol = sum(bar.volume or 0 for bar in self.bars)
        if total_vol == 0:
            return 0.0

        return sum(bar.close * (bar.volume or 0) for bar in self.bars) / total_vol

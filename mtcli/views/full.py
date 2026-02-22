# mtcli/views/full.py

class FullView:
    """
    View completa de barras.

    Exibe:
    - timestamp
    - OHLC
    - range
    - body
    - estrutura em relação ao candle anterior
    """

    def __init__(self, bars, period, **_):
        self.bars = bars
        self.period = period

    def render(self) -> list[str]:
        lines: list[str] = []

        for bar in self.bars:
            ts = bar.timestamp.strftime("%Y-%m-%d %H:%M")
            line = (
                f"{ts} "
                f"O:{bar.open:.0f} H:{bar.high:.0f} "
                f"L:{bar.low:.0f} C:{bar.close:.0f} "
                f"R:{bar.range:.0f} B:{bar.body:.0f} "
                f"{bar.structure_symbol}"
            )
            lines.append(line)

        return lines

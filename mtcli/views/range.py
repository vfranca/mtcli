# mtcli/views/range.py

class RangeView:
    """
    View focada em range e estrutura.
    """

    def __init__(self, bars, period, **_):
        self.bars = bars
        self.period = period

    def render(self) -> list[str]:
        lines: list[str] = []

        for bar in self.bars:
            ts = bar.timestamp.strftime("%H:%M")
            line = (
                f"{ts} "
                f"R:{bar.range:.0f} "
                f"B:{bar.body:.0f} "
                f"{bar.structure_symbol}"
            )
            lines.append(line)

        return lines

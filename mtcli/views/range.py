from mtcli.views.base import BaseView


class RangeView(BaseView):
    """View focada em range e sombras do candle."""

    def render(self) -> list[str]:
        lines = []
        for i, bar in enumerate(self.bars, start=1):
            line = (
                f"{self.prefix(i)}"
                f"R:{bar.range:.0f} "
                f"U:{bar.upper_tail:.0f} "
                f"L:{bar.lower_tail:.0f}"
                f"{self.suffix(bar)}"
            )
            lines.append(line)
        return lines

from mtcli.views.base import BaseView


class FullView(BaseView):
    """View detalhada com range, corpo e direção."""

    def render(self) -> list[str]:
        lines = []
        for i, bar in enumerate(self.bars, start=1):
            direction = "↑" if bar.is_bullish else "↓"
            line = (
                f"{self.prefix(i)}"
                f"O:{bar.open:.0f} H:{bar.high:.0f} "
                f"L:{bar.low:.0f} C:{bar.close:.0f} "
                f"R:{bar.range:.0f} B:{bar.body:.0f} {direction}"
                f"{self.suffix(bar)}"
            )
            lines.append(line)
        return lines

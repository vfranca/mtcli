from mtcli.views.base import BaseView


class MinView(BaseView):
    """View compacta (OHLC resumido)."""

    def render(self) -> list[str]:
        lines = []
        for i, bar in enumerate(self.bars, start=1):
            line = (
                f"{self.prefix(i)}"
                f"{bar.open:.0f} {bar.high:.0f} {bar.low:.0f} {bar.close:.0f}"
                f"{self.suffix(bar)}"
            )
            lines.append(line)
        return lines

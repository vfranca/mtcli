from mtcli.views.base import BaseView


class RateView(BaseView):
    """View de variação absoluta e direcional."""

    def render(self) -> list[str]:
        lines = []
        for i, bar in enumerate(self.bars, start=1):
            delta = bar.close - bar.open
            direction = "+" if delta >= 0 else "-"
            line = (
                f"{self.prefix(i)}"
                f"Δ:{abs(delta):.0f}{direction}"
                f"{self.suffix(bar)}"
            )
            lines.append(line)
        return lines

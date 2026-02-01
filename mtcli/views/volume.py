from mtcli.views.base import BaseView


class VolumeView(BaseView):
    """View focada em volume negociado."""

    def render(self) -> list[str]:
        lines = []
        for i, bar in enumerate(self.bars, start=1):
            vol = bar.volume or 0
            line = (
                f"{self.prefix(i)}"
                f"C:{bar.close:.0f} V:{vol}"
                f"{self.suffix(bar)}"
            )
            lines.append(line)
        return lines

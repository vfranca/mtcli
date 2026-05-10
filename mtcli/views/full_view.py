"""
View completa de barras (FullView).

Exibe:
- timestamp (opcional via BaseView)
- estrutura (ASC/DESC/INT/EXT)
- body
- OHLC
- range

Voltada para análise detalhada de price action.
"""

from ..conf import DIGITS
from .base_view import BaseView


class FullView(BaseView):
    """
    Renderização completa de barras OHLC.
    """

    def render(self) -> list[str]:
        lines: list[str] = []

        for i, bar in enumerate(self.bars, 1):
            line = self.prefix(i)
            line += (
                f"{bar.structure_symbol} "
                f"{bar.body:.{DIGITS}f} "
                f"{bar.high:.{DIGITS}f} "
                f"{bar.low:.{DIGITS}f} "
                f"{bar.close:.{DIGITS}f} "
                f"R{bar.range:.{DIGITS}f}"
            )
            line += self.suffix(bar)

            lines.append(line)

        return lines

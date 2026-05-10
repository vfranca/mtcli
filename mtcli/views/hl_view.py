"""
View HL (High/Low).

Exibe:
- estrutura da barra
- máxima
- mínima
"""

from ..conf import DIGITS
from .base_view import BaseView


class HlView(BaseView):
    """
    Renderização simplificada de barras (HL).
    """

    def render(self) -> list[str]:
        lines: list[str] = []

        for i, bar in enumerate(self.bars, 1):
            line = self.prefix(i)
            line += (
                f"{bar.structure_symbol} "
                f"{bar.high:.{DIGITS}f} {bar.low:.{DIGITS}f}"
            )
            line += self.suffix(bar)

            lines.append(line)

        return lines

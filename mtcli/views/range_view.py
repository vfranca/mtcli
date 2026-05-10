"""
View de Range.

Exibe:
- estrutura da barra (ASC/DESC/INT/EXT)
- range (high - low)

Útil para:
- análise de volatilidade
- detecção de compressão/expansão
- identificação de grind vs impulso
"""

from .base_view import BaseView
from ..conf import DIGITS


class RangeView(BaseView):
    """
    Renderização simplificada focada em range.
    """

    def __init__(self, bars, period, **kwargs):
        """
        Mantém compatibilidade com ViewFactory.
        """
        super().__init__(bars, period, **kwargs)

    def render(self) -> list[str]:
        if not self.bars:
            return ["<no data>"]

        lines: list[str] = []

        for i, bar in enumerate(self.bars, 1):
            line = self.prefix(i)

            line += (
                f"{bar.structure_symbol} "
                f"{bar.range:.{DIGITS}f}"
            )

            line += self.suffix(bar)

            lines.append(line)

        return lines

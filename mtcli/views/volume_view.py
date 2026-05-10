"""
View de Volume.

Exibe:
- estrutura da barra (ASC/DESC/INT/EXT)
- volume (tick ou real)

Útil para:
- validação de movimentos (volume confirma direção?)
- detecção de exaustão (alto volume sem continuidade)
- análise de absorção
"""

from .base_view import BaseView


class VolumeView(BaseView):
    """
    Renderização focada em volume.
    """

    def __init__(self, bars, period, volume=None, **kwargs):
        """
        Args:
            volume (str | None): "real" ou "tick"
        """
        super().__init__(bars, period, volume=volume, **kwargs)

    # ---------------- helper ---------------- #

    def _get_volume(self, bar):
        """
        Seleciona tipo de volume conforme configuração.
        """
        if self.volume == "real":
            return bar.real_volume
        return bar.tick_volume

    # ---------------- render ---------------- #

    def render(self) -> list[str]:
        if not self.bars:
            return ["<no data>"]

        lines: list[str] = []

        for i, bar in enumerate(self.bars, 1):
            vol = self._get_volume(bar)
            vol_str = f"{vol}" if vol is not None else "-"

            line = self.prefix(i)

            line += (
                f"{bar.structure_symbol} "
                f"{vol_str}"
            )

            line += self.suffix(bar)

            lines.append(line)

        return lines

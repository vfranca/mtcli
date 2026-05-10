"""
Classe base para renderização de barras no terminal.

Define:
- interface padrão de views (render)
- utilitários comuns (prefixo, sufixo)
- configuração compartilhada (period, flags, etc)

Todas as views devem herdar desta classe.
"""

from typing import List
from mtcli.models.bars_model import BarModel


class BaseView:
    """
    Classe base para todas as views de barras.

    Fornece helpers para:
    - numeração de linhas
    - formatação de timestamp
    """

    def __init__(
        self,
        bars: list[BarModel],
        period: str,
        numerator: bool = False,
        show_date: bool = False,
        volume: str | None = None,
    ):
        """
        Args:
            bars (list[BarModel]): Barras já processadas
            period (str): Timeframe (M1, M5, D1, etc)
            numerator (bool): Exibir índice da barra
            show_date (bool): Exibir timestamp completo
            volume (str | None): Tipo de volume (tick/real)
        """
        self.bars = bars
        self.period = period
        self.numerator = numerator
        self.show_date = show_date
        self.volume = volume

    # ---------------- helpers ---------------- #

    def prefix(self, index: int) -> str:
        """
        Prefixo opcional com numeração da barra.
        """
        return f"{index} " if self.numerator else ""

    def suffix(self, bar: BarModel) -> str:
        """
        Sufixo opcional com timestamp.

        Regras:
        - intraday → HH:MM
        - diário/semanal → YYYY-MM-DD
        """
        if not self.show_date:
            return ""

        if self.period.lower() in {"d1", "w1", "mn1"}:
            return f" {bar.timestamp.date()}"

        return f" {bar.timestamp.strftime('%H:%M')}"

    # ---------------- contrato ---------------- #

    def render(self) -> List[str]:
        """
        Renderiza barras para saída textual.

        Returns:
            List[str]: Linhas prontas para CLI
        """
        raise NotImplementedError("Views devem implementar render()")

# mtcli/views/min.py

class MinView:
    """
    View mínima de barras.

    Exibe:
    - horário
    - fechamento
    - estrutura do candle
    """

    def __init__(self, bars, period, show_date=False, **_):
        self.bars = bars
        self.show_date = show_date

    def render(self) -> list[str]:
        lines: list[str] = []

        for bar in self.bars:
            ts_fmt = "%Y-%m-%d %H:%M" if self.show_date else "%H:%M"
            ts = bar.timestamp.strftime(ts_fmt)

            line = (
                f"{ts} "
                f"C:{bar.close:.0f} "
                f"{bar.structure_symbol}"
            )
            lines.append(line)

        return lines

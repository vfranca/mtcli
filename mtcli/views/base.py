class BaseView:
    """
    View base para renderização de barras no terminal.
    """

    def __init__(self, bars, period, numerator=False, show_date=False, volume=None):
        self.bars = bars
        self.period = period
        self.numerator = numerator
        self.show_date = show_date
        self.volume = volume

    def prefix(self, index: int) -> str:
        return f"{index} " if self.numerator else ""

    def suffix(self, bar) -> str:
        if not self.show_date:
            return ""

        if self.period in {"d1", "w1", "mn1"}:
            return f" {bar.date}"
        return f" {bar.time}"

    def render(self) -> list[str]:
        raise NotImplementedError

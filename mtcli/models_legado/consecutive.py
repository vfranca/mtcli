from mtcli.models.bar import BarModel


class ConsecutiveBarsModel:
    """
        Agrupa barras consecutivas na mesma direção.
    """

    def __init__(self, bars: list[BarModel]):
        self.bars = bars

    def group(self) -> list[list[BarModel]]:
        """
            Retorna listas de barras consecutivas.
        """
        if not self.bars:
            return []

        groups = [[self.bars[0]]]

        for bar in self.bars[1:]:
            last = groups[-1][-1]

            if bar.is_bullish == last.is_bullish:
                groups[-1].append(bar)
            else:
                groups.append([bar])

        return groups

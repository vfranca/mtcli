# mtcli/views/volume.py

class VolumeView:
    """
    View focada em volume e estrutura do candle.
    """

    def __init__(self, bars, period, volume=None, **_):
        self.bars = bars
        self.volume_mode = volume

    def render(self) -> list[str]:
        lines: list[str] = []

        for bar in self.bars:
            ts = bar.timestamp.strftime("%H:%M")

            vol = (
                bar.real_volume
                if self.volume_mode == "real"
                else bar.tick_volume
            )

            vol_str = f"V:{vol}" if vol is not None else "V:-"

            line = (
                f"{ts} "
                f"{vol_str} "
                f"{bar.structure_symbol}"
            )
            lines.append(line)

        return lines

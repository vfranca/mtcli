from mtcli.models.signals_model import SignalsModel


class bar_mock:
    def __init__(self, high, low, close, volume, volume_real, body, top, bottom, trend):
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.volume_real = volume_real
        self.body = body
        self.top = top
        self.bottom = bottom
        self.trend = trend


bars_mock = [
    bar_mock(140500, 138900, 140200, 1000, 1500, 80, 10, 10, "verde"),
    bar_mock(141500, 139800, 141200, 2000, 3000, 10, 10, 80, "verde"),
    bar_mock(140500, 138900, 139000, 1800, 2800, 10, 80, 10, "vermelho"),
    bar_mock(140200, 139100, 139800, 4000, 5000, 80, 10, 10, "verde"),
    bar_mock(141500, 138800, 141300, 3000, 3500, 10, 10, 80, "verde"),
    bar_mock(140500, 138900, 139200, 2000, 2500, 10, 80, 10, "vermelho"),
]


def test_obtem_lista_de_sinais():
    sinais = SignalsModel(bars_mock).get_sinais()
    result = [(sinal) for sinal in sinais]
    assert result[:3] == [
        ["rompimento", "", "", "", ""],
        ["doji", "ascendente", "gap de alta", "", "volume ascendente"],
        ["doji", "descendente", "gap de baixa", "", "volume descendente"],
    ]

from mtcli.models.model_signals import SignalsModel


class bar:
    def __init__(self, high, low, close, body, top, bottom, trend):
        self.high = high
        self.low = low
        self.close = close
        self.body = body
        self.top = top
        self.bottom = bottom
        self.trend = trend


bars = [
    bar(140500, 138900, 140200, 80, 10, 10, "verde"),
    bar(141500, 139800, 141200, 10, 10, 80, "verde"),
    bar(140500, 138900, 139000, 10, 80, 10, "vermelho"),
    bar(140200, 139100, 139800, 80, 10, 10, "verde"),
    bar(141500, 138800, 141300, 10, 10, 80, "verde"),
    bar(140500, 138900, 139200, 10, 80, 10, "vermelho"),
]


def test_obtem_lista_de_sinais():
    sinais = SignalsModel(bars).get_sinais()
    result = [(sinal) for sinal in sinais]
    assert result[:3] == [
        ["rompimento"],
        ["doji", "ascendente", "gap de alta"],
        ["doji", "descendente", "gap de baixa"],
    ]

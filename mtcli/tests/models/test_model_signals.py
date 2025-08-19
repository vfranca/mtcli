from mtcli.models.model_signals import SignalsModel


class bar:
    def __init__(self, high, low, body, top, bottom):
        self.high = high
        self.low = low
        self.body = body
        self.top = top
        self.bottom = bottom


bars = [
    bar(140500, 138900, 80, 10, 10),
    bar(141500, 139800, 10, 10, 80),
    bar(140500, 138900, 10, 80, 10),
    bar(140200, 139100, 80, 10, 10),
    bar(141500, 138800, 10, 10, 80),
    bar(140500, 138900, 10, 80, 10),
]


def test_obtem_lista_de_sinais_de_uma_barra():
    sinais = SignalsModel(bars).get_sinais_de_uma_barra()
    result = [(sinal) for sinal in sinais]
    assert result[:3] == ["rompimento", "doji", "doji"]


def test_obtem_lista_de_sinais_de_duas_barras():
    sinais = SignalsModel(bars).get_sinais_de_duas_barras()
    result = [(sinal) for sinal in sinais]
    assert result[:5] == [None, "ascendente", "descendente", "interna", "externa"]

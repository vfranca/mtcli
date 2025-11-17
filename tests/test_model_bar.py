from mtcli.models.bar_model import BarModel

rate = [
    "2015.04.01 12:40:00",
    "51187.00000",
    "56965.00000",
    "51187.00000",
    "56229.00000",
    "14628859",
    "8158109400",
]

bar = BarModel(rate)


def test_retorna_a_data():
    assert str(bar.date) == "2015-04-01"


def test_retorna_a_hora():
    assert str(bar.time) == "12:40"


def test_retorna_a_abertura():
    assert bar.open == 51187.0


def test_retorna_a_maxima():
    assert bar.high == 56965.0


def test_retorna_a_minima():
    assert bar.low == 51187.0


def test_retorna_o_fechamento():
    assert bar.close == 56229.0


def test_retorna_o_volume_de_negocios():
    assert bar.volume == 14628859


def test_retorna_o_tamanho():
    assert bar.range == 5778.0


def test_retorna_o_percentual_do_corpo():
    assert bar.body == 87


def test_retorna_o_percentual_da_sombra_superior():
    assert bar.top == 13


def test_retorna_o_percentual_da_sombra_inferior():
    assert bar.bottom == 0


def test_retorna_o_tamanho_do_corpo():
    assert bar.body_range == 5042.0


def test_retorna_a_tendencia():
    assert bar.trend == "bull"

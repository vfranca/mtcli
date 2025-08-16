import pytest

from mtcli.extensions.moving_average.models import model_ma

rate = [
    "2024.11.11 13:55:00",
    "5853.5",
    "5621.0",
    "up",
    "24",
    "5.0",
    "20",
    "MODE_EMA",
    "PRICE_CLOSE",
]

ma = model_ma.MaModel(rate)


@pytest.mark.skip(reason="extensão desativada")
def test_retorna_a_data():
    assert str(ma.date) == "2024-11-11"


@pytest.mark.skip(reason="extensão desativada")
def test_retorna_a_hora():
    assert str(ma.time) == "13:55:00"


@pytest.mark.skip(reason="extensão desativada")
def test_retorna_o_fechamento():
    assert ma.close == 5853.5


@pytest.mark.skip(reason="extensão desativada")
def test_retorna_a_media_movel():
    assert ma.ma == 5621.0


@pytest.mark.skip(reason="extensão desativada")
def test_retorna_a_inclinacao():
    assert ma.inclinacao == "up"


@pytest.mark.skip(reason="extensão desativada")
def test_retorna_a_variacao():
    assert ma.variacao == 24


@pytest.mark.skip(reason="extensão desativada")
def test_retorna_a_variacao_flat():
    assert ma.variacao_flat == 5.0


@pytest.mark.skip(reason="extensão desativada")
def test_retorna_a_quantidade_de_periodos():
    assert ma.count == 20


@pytest.mark.skip(reason="extensão desativada")
def test_retorna_o_modo():
    assert ma.mode == "MODE_EMA"


@pytest.mark.skip(reason="extensão desativada")
def test_retorna_o_preco_de_aplicacao():
    assert ma.price == "PRICE_CLOSE"

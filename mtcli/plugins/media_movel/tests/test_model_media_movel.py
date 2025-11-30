from ..model import MediaMovelModel


def test_sma():
    assert MediaMovelModel([10, 20, 30], 3).calcula_sma() == [20.0]


def test_ema():
    assert MediaMovelModel([10, 20, 30], 3).calcula_ema() == [20.0]

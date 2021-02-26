from mtcli.bar import Bar


rate = [
    "2015.04.01",
    "51187.00000",
    "56965.00000",
    "51187.00000",
    "56229.00000",
    "14628859",
    "8158109400",
]
rates = Bar(rate)


def test_date():
    assert rates.date == "2015.04.01"


def test_open():
    assert rates.open == 51187.0


def test_high():
    assert rates.high == 56965.0


def test_low():
    assert rates.low == 51187.0


def test_close():
    assert rates.close == 56229.0


def test_volume():
    assert rates.volume == 14628859


def test_range():
    assert rates.range == 5778.0


def test_body():
    assert rates.body == 87


def test_top():
    assert rates.top == 13


def test_bottom():
    assert rates.bottom == 0


def test_range_body():
    assert rates.body_range == 5042.0


def test_trend():
    assert rates.trend == "VERDE"

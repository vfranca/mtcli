from mtcli import rate_model

row_fixture = [
    "2015.04.01",
    "51187.00000",
    "56965.00000",
    "51187.00000",
    "56229.00000",
    "14628859",
    "8158109400",
    "50089.0",
    "flat8",
    "51089.0",
    "down20",
    "52089.0",
    "up25",
]

rate = rate_model.RateModel(row_fixture)


def test_date():
    assert rate.date == "2015.04.01"


def test_open():
    assert rate.open == 51187.0


def test_high():
    assert rate.high == 56965.0


def test_low():
    assert rate.low == 51187.0


def test_close():
    assert rate.close == 56229.0


def test_ticks():
    assert rate.ticks == 14628859


def test_volume():
    assert rate.volume == 8158109400


def test_valor_da_mm_curta():
    assert rate.mm_curta == 50089.0


def test_direcao_da_mm_curta():
    assert rate.mm_curta_direcao == "flat8"


def test_valor_da_mm_intermediaria():
    assert rate.mm_intermediaria == 51089.0


def test_direcao_da_mm_intermediaria():
    assert rate.mm_intermediaria_direcao == "down20"


def test_valor_da_mm_longa():
    assert rate.mm_longa == 52089.0


def test_direcao_da_mm_longa():
    assert rate.mm_longa_direcao == "up25"


def test_range():
    assert rate.range == 5778.0


def test_body():
    assert rate.body == 87


def test_top():
    assert rate.top == 13


def test_bottom():
    assert rate.bottom == 0


def test_range_body():
    assert rate.body_range == 5042.0


def test_trend():
    assert rate.trend == "VERDE"

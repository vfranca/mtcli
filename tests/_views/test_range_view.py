import pytest
from mtcli._views import range_view

data_set = [
    {
        "channel_trend": "ASC",
        "range": 0.28
    }
]
view = range_view.RangeView(data_set)


def test_saida_da_view():
    expec = "ASC 0.28"
    assert view.view == expec

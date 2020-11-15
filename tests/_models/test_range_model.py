import pytest
from mtcli._models import range_model

model = range_model.RangeModel("abev3", "daily", 1)


#@pytest.mark.skip()
def test_dataset_do_model():
    expec = [
        {"high": 18.57, "low": 18.29, "range": 0.28000000000000114,},
    ]
    assert model.data_set == expec

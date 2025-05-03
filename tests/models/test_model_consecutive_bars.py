from mtcli.models import model_consecutive_bars
from mtcli import conf

consecutive = model_consecutive_bars.ConsecutiveBarsModel(
    [50, 60], [10, 20], [40, 50], [60, 80], [5, 15], [500, 700]
)


def test_retorna_gap_de_fechamento():
    consecutive = model_consecutive_bars.ConsecutiveBarsModel(
        [-50, -60], [90, 40], [20, 10], [80, 60], [15, 5]
    )
    assert consecutive.gap() == 5.00


def test_exibe_alteracao_no_volume():
    assert consecutive.volume() == conf.alta

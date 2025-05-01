import unittest
from mtcli.models import model_consecutive_bars
from mtcli import conf


class TestConsecutiveBarsModel(unittest.TestCase):
    def setUp(self):
        self.o = model_consecutive_bars.ConsecutiveBarsModel(
            [50, 60], [10, 20], [40, 50], [60, 80], [5, 15]
        )

    def test_retorna_os_fechamentos(self):
        self.assertEqual(self.o.close, [40, 50])

    def test_retorna_as_maximas(self):
        self.assertEqual(self.o.high, [60, 80])

    def test_retorna_as_minimas(self):
        self.assertEqual(self.o.low, [5, 15])

    def test_retorna_gap_de_fechamento(self):
        o = model_consecutive_bars.ConsecutiveBarsModel(
            [-50, -60], [90, 40], [20, 10], [80, 60], [15, 5]
        )
        self.assertEqual(o.get_gap(), 5.00)


if __name__ == "__main__":
    unittest.main()

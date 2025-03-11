import unittest
from mtcli.pa.pattern import OneBar
from mtcli import conf


class TestPaOneBar(unittest.TestCase):
    def test_body_pattern_bull(self):
        o = OneBar(50, 25, 25, 92600, 92500)
        self.assertEqual(o.body_pattern, conf.alta)

    def test_body_pattern_bear(self):
        o = OneBar(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.body_pattern, conf.baixa)

    def test_body_pattern_doji(self):
        o = OneBar(-5, 50, 45, 92500, 92600)
        self.assertEqual(o.body_pattern, conf.lateral)

    def test_tail_top(self):
        o = OneBar(-50, 20, 30, 92500, 92600)
        self.assertEqual(o.tail, conf.sombra_inferior)

    def test_tail_bottom(self):
        o = OneBar(-50, 30, 20, 92500, 92600)
        self.assertEqual(o.tail, conf.sombra_superior)

    def test_tail_neutral(self):
        o = OneBar(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.tail, "")

    def test_buy_pressure(self):
        o = OneBar(50, 20, 30, 92700, 92600)
        self.assertEqual(o.pattern, conf.rompimento_alta)

    def test_sell_pressure(self):
        o = OneBar(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.pattern, conf.rompimento_baixa)


if __name__ == "__main__":
    unittest.main()

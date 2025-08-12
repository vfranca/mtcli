import unittest

from mtcli import conf
from mtcli.models import model_unconsecutive_bar


class TestUnconsecutiveBarModel(unittest.TestCase):
    def test_retorna_barra_de_alta(self):
        o = model_unconsecutive_bar.UnconsecutiveBarModel(50, 25, 25, 92600, 92500)
        self.assertEqual(o.get_body(), conf.alta)

    def test_retorna_barra_de_baixa(self):
        o = model_unconsecutive_bar.UnconsecutiveBarModel(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.get_body(), conf.baixa)

    def test_retorna_barra_doji(self):
        o = model_unconsecutive_bar.UnconsecutiveBarModel(-5, 50, 45, 92500, 92600)
        self.assertEqual(o.get_body(), conf.lateral)

    def test_retorna_sombra_superior(self):
        o = model_unconsecutive_bar.UnconsecutiveBarModel(-50, 20, 30, 92500, 92600)
        self.assertEqual(o.get_tail(), conf.sombra_inferior)

    def test_retorna_sombra_inferior(self):
        o = model_unconsecutive_bar.UnconsecutiveBarModel(-50, 30, 20, 92500, 92600)
        self.assertEqual(o.get_tail(), conf.sombra_superior)

    def test_retorna_sem_sombra(self):
        o = model_unconsecutive_bar.UnconsecutiveBarModel(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.get_tail(), "")

    def test_retorna_barra_de_rompimento_de_alta(self):
        o = model_unconsecutive_bar.UnconsecutiveBarModel(50, 20, 30, 92700, 92600)
        self.assertEqual(o.get_breakout(), conf.rompimento_alta)

    def test_retorna_barra_de_rompimento_de_baixa(self):
        o = model_unconsecutive_bar.UnconsecutiveBarModel(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.get_breakout(), conf.rompimento_baixa)


if __name__ == "__main__":
    unittest.main()

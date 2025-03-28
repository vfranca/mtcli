import unittest
from mtcli.pa import pattern
from mtcli import conf


class TestPaOneBar(unittest.TestCase):
    def test_retorna_barra_de_alta(self):
        o = pattern.OneBar(50, 25, 25, 92600, 92500)
        self.assertEqual(o.body_pattern, conf.alta)

    def test_retorna_barra_de_baixa(self):
        o = pattern.OneBar(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.body_pattern, conf.baixa)

    def test_retorna_barra_doji(self):
        o = pattern.OneBar(-5, 50, 45, 92500, 92600)
        self.assertEqual(o.body_pattern, conf.lateral)

    def test_retorna_sombra_superior(self):
        o = pattern.OneBar(-50, 20, 30, 92500, 92600)
        self.assertEqual(o.tail, conf.sombra_inferior)

    def test_retorna_sombra_inferior(self):
        o = pattern.OneBar(-50, 30, 20, 92500, 92600)
        self.assertEqual(o.tail, conf.sombra_superior)

    def test_retorna_sem_sombra(self):
        o = pattern.OneBar(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.tail, "")

    def test_retorna_barra_de_rompimento_de_alta(self):
        o = pattern.OneBar(50, 20, 30, 92700, 92600)
        self.assertEqual(o.pattern, conf.rompimento_alta)

    def test_retorna_barra_de_rompimento_de_baixa(self):
        o = pattern.OneBar(-50, 25, 25, 92500, 92600)
        self.assertEqual(o.pattern, conf.rompimento_baixa)


class TestTwoBars(unittest.TestCase):
    def setUp(self):
        self.o = pattern.TwoBars([50, 60], [10, 20], [40, 50], [60, 80], [5, 15])

    def test_retorna_os_fechamentos(self):
        self.assertEqual(self.o.close, [40, 50])

    def test_retorna_as_maximas(self):
        self.assertEqual(self.o.high, [60, 80])

    def test_retorna_as_minimas(self):
        self.assertEqual(self.o.low, [5, 15])

    def test_retorna_gap_de_fechamento(self):
        o = pattern.TwoBars([-50, -60], [90, 40], [20, 10], [80, 60], [15, 5])
        self.assertEqual(o.pattern, "%s5.00" % "G")


if __name__ == "__main__":
    unittest.main()

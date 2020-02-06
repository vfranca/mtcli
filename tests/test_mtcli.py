from unittest import TestCase, mock
from mtcli.mtcli import controller


class TestMTCli(TestCase):
    @mock.patch("mtcli.mtcli._view")
    def test_controlador_retorna_view_default(self, view):
        view.brooks_view.return_value = (
            " ASC  DOJI7R0.02  TOP64 18.57 18.29 18.37MP18.43 R0.28 -0.38"
        )
        self.assertEqual(
            controller("ABEV3", "Daily", "", "", 1),
            [" ASC  DOJI7R0.02  TOP64 18.57 18.29 18.37MP18.43 R0.28 -0.38"],
        )

    @mock.patch("mtcli.mtcli._view")
    def test_controlador_retorna_views_de_canal(self, view):
        view.channel_view.return_value = " ASC 18.57 18.29"
        self.assertEqual(
            controller("ABEV3", "Daily", "ch", "", 1), [" ASC 18.57 18.29"]
        )

    @mock.patch("mtcli.mtcli._view")
    def test_controlador_retorna_views_de_fechamento(self, view):
        view.close_view.return_value = "18.37"
        self.assertEqual(controller("ABEV3", "Daily", "c", "", 1), ["18.37"])

    @mock.patch("mtcli.mtcli._view")
    def test_controlador_retorna_views_de_maxima(self, view):
        view.high_view.return_value = "18.57"
        self.assertEqual(controller("ABEV3", "Daily", "h", "", 1), ["18.57"])

    @mock.patch("mtcli.mtcli._view")
    def test_controlador_retorna_views_de_minima(self, view):
        view.low_view.return_value = "18.29"
        self.assertEqual(controller("ABEV3", "Daily", "l", "", 1), ["18.29"])

    @mock.patch("mtcli.mtcli._view")
    def test_controlador_retorna_views_de_range(self, view):
        view.range_view.return_value = " ASC VERMELHO 0.28"
        self.assertEqual(
            controller("ABEV3", "Daily", "r", "", 1), [" ASC VERMELHO 0.28"]
        )

    @mock.patch("mtcli.mtcli._view")
    def test_controlador_retorna_views_de_volume(self, view):
        view.volume_view.return_value = " ASC VERMELHO 16466"
        self.assertEqual(
            controller("ABEV3", "Daily", "vol", "", 1), [" ASC VERMELHO 16466"]
        )

    @mock.patch("mtcli.mtcli._view")
    def test_controlador_retorna_views_de_variacao_percentual(self, view):
        view.var_view.return_value = " ASC -0.38"
        self.assertEqual(controller("ABEV3", "Daily", "var", "", 1), [" ASC -0.38"])

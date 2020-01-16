from unittest import TestCase, mock
from mtcli.mtcli import controller


class TestController(TestCase):
    @mock.patch("mtcli.mtcli._view")
    def test_controlador_retorna_view_default(self, view):
        view.brooks_view.return_value = (
            " ASC  DOJI7R0.02  TOP64 18.57 18.29 18.37MP18.43 R0.28 -0.38"
        )
        self.assertEqual(
            controller("ABEV3", "Daily", "", "", 1),
            [" ASC  DOJI7R0.02  TOP64 18.57 18.29 18.37MP18.43 R0.28 -0.38"],
        )

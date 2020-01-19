from unittest import TestCase, mock
from mtcli.pymql5_facade import PyMQL5Facade


class TestPyMQL5Facade(TestCase):
    def setUp(self):
        self.facade = PyMQL5Facade("ABEV3", "Daily")

    @mock.patch("mtcli.pymql5_facade.mql5")
    def test_obtem_fechamento_da_barra(self, mql5):
        mql5.iClose.return_value = 18.50
        self.assertEqual(self.facade.get_close(), 18.50)

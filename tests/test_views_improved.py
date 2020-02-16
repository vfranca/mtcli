from unittest import TestCase
from mtcli.views_improved import DefaultView


class TestViews(TestCase):
    def setUp(self):
        self.bars = []

    def test_retorna_view_default(self):
        res = DefaultView()
        res = res.show_list(self.bars)
        expec = ""
        self.assertEqual(res, expec)

from unittest import TestCase
from trade.src.chart import *

class ChartTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"

    def test_chart_reader(self):
        self.assertTrue(chart_reader(self.file), "Retorno da função chart_reader")

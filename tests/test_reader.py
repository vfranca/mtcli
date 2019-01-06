from unittest import TestCase
from trade.reader import *

class ReaderTestCase(TestCase):

    def setUp(self):
        self.file = "tests/fixtures/var/wing19m5.csv"
    
    def test_reader(self):
        self.assertTrue(reader(self.file, 1), "A função reader() deve retornar uma lista de barras")

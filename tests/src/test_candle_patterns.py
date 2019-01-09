from unittest import TestCase
from trade.src.candle_patterns import *

class CandlePatternsTestCase(TestCase):

    def setUp(self):
        pass

    def test_is_hammer(self):
        self.assertTrue(is_hammer(10,5,85), "Verifica se o padrão é martelo")
        self.assertTrue(is_hammer(25,24,75), "Verifica se o padrão é martelo")
        self.assertFalse(is_hammer(0,25,75), "Verifica se o padrão é martelo")
        self.assertFalse(is_hammer(10,30,60), "Verifica se o padrão é martelo")
        self.assertTrue(is_hammer(-10,5,85), "Verifica se o padrão é martelo")
        self.assertTrue(is_hammer(-25,24,75), "Verifica se o padrão é martelo")
        self.assertFalse(is_hammer(-10,30,60), "Verifica se o padrão é martelo")
        self.assertFalse(is_hammer(-40,0,60), "Verifica se o padrão é martelo")

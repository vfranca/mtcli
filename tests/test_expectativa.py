from unittest import TestCase
from trade.expec import *

class ExpecTestCase(TestCase):

    def test_expectativa_matematica(self):
        self.assertEqual(get_expec(50, 50, 25), 12.5)
    
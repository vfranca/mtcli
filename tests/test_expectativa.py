#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from cli_trade.expec import *


class ExpecTestCase(TestCase):

    def test_expectativa_matematica(self):
        self.assertEqual(get_expec(50, 50, 25), 12.5)

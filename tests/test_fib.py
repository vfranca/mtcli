#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from cli_trade._fib import Fib


class FibTestCase(TestCase):

    def setUp(self):
        self.obj = Fib(88900.0, 87200.0, "h")
        self.obj1 = Fib(88900.0, 87200.0)
        self.obj2 = Fib(88900.0, 87200.0, "l")

    def test_high(self):
        self.assertEqual(self.obj.h, 88900, "Máxima do movimento")
        self.assertEqual(self.obj1.h, 88900, "Máxima do movimento")
        self.assertEqual(self.obj2.h, 88900, "Máxima do movimento")

    def test_low(self):
        self.assertEqual(self.obj.l, 87200, "Mínima do movimento")
        self.assertEqual(self.obj1.l, 87200, "Mínima do movimento")
        self.assertEqual(self.obj2.l, 87200, "Mínima do movimento")

    def test_retracao_38(self):
        self.assertEqual(self.obj.r38, 88250.6, "Retração de 0.382 de Fibonacci")
        self.assertEqual(self.obj1.r38, 88250.6, "Retração de 0.382 de Fibonacci")
        self.assertEqual(self.obj2.r38, 87849.4, "Retração de 0.382 de Fibonacci")

    def test_retracao_50(self):
        self.assertEqual(self.obj.r, 88050, "Retração de 0.50 de Fibonacci")
        self.assertEqual(self.obj1.r, 88050, "Retração de 0.50 de Fibonacci")
        self.assertEqual(self.obj2.r, 88050, "Retração de 0.50 de Fibonacci")

    def test_retracao_61(self):
        self.assertEqual(self.obj.r61, 87849.4, "Retração de 0,618 de Fibonacci")
        self.assertEqual(self.obj1.r61, 87849.4, "Retração de 0,618 de Fibonacci")
        self.assertEqual(self.obj2.r61, 88250.6, "Retração de 0,618 de Fibonacci")

    def test_extensao_61(self):
        self.assertEqual(self.obj.e61, 89950.6, "Extensão de 1.618 de Fibonacci")
        self.assertEqual(self.obj1.e61, 89950.6, "Extensão de 1.618 de Fibonacci")
        self.assertEqual(self.obj2.e61, 86149.4, "Extensão de 1.618 de Fibonacci")

    def test_extensao_50(self):
        self.assertEqual(self.obj.e, 89750, "Extensão de 0.50")
        self.assertEqual(self.obj1.e, 89750, "Extensão de 0.50")
        self.assertEqual(self.obj2.e, 86350, "Extensão de 0.50")

    def test_saida_texto(self):
        self.assertEqual(self.obj.__str__(), "87849.40 88050.00 88250.60 > 89549.40 89750.00 89950.60")
        self.assertEqual(self.obj2.__str__(), "88250.60 88050.00 87849.40 > 86550.60 86350.00 86149.40")

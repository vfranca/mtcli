#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cli_trade.src.fib import Fib
import sys


high = float(sys.argv[1])
low = float(sys.argv[2])
trend = str(sys.argv[3])

print(Fib(high, low, trend))

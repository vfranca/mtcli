#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cli_trade.cli_trade import controller
from cli_trade.sma import ma
from cli_trade.ema import get_ema
from cli_trade._fib import Fib
from cli_trade.atr import atr
from cli_trade.conf import *
import sys
import re


if sys.argv[1] == "bars":
    file = csv_path
    pattern_qtt = re.compile(r'^[0-9]*$')
    pattern_date = re.compile(r'^[0-9]{4}.[0-9]{2}.[0-9]{2}$')
    pattern_view = re.compile('^[a-z]*$')
    # chamada com 1 argumento
    if len(sys.argv) == 3:
        file += sys.argv[2]
        views = controller(file)
    # chamada com 2 argumentos
    elif len(sys.argv) == 4:
        file += sys.argv[2]
        arg2 = sys.argv[3]
        if pattern_qtt.match(arg2):
            views = controller(file, qtt_bars = int(arg2))
        elif pattern_date.match(arg2):
            views = controller(file, date = arg2)
        elif pattern_view.match(arg2):
            views = controller(file, view = arg2)
    # chamada com 3 argumentos
    elif len(sys.argv) == 5:
        file += sys.argv[2]
        arg2 = sys.argv[3]
        arg3 = sys.argv[4]
        # Quando o 2o argumento é uma data
        if pattern_date.match(arg2):
            if pattern_qtt.match(arg3):
                views = controller(file, date = arg2, qtt_bars = int(arg3))
            if pattern_view.match(arg3):
                views = controller(file, date = arg2, view = arg3)
        # Quando o 2o argumento é um modo de exibição
        elif pattern_view.match(arg2):
            if pattern_qtt.match(arg3):
                views = controller(file, view = arg2, qtt_bars = int(arg3))
            elif pattern_date.match(arg3):
                views = controller(file, view = arg2, date = arg3)
    for view in views:
        print(view)

if sys.argv[1] == "sma":
    times = int(sys.argv[2])
    filename = csv_path + sys.argv[3]
    mms = ma(times, filename)
    print(mms)

if sys.argv[1] == "ema":
    times = int(sys.argv[2])
    filename = csv_path + sys.argv[3]
    mm = get_ema(times, filename)
    print(mm)

if sys.argv[1] == "atr":
    file = "%s%s.csv" % (csv_path, sys.argv[2])
    if len(sys.argv) == 4:
        candles = int(sys.argv[3])
    else:
        candles = 14
    atr = atr(file, candles)
    print(atr)

if sys.argv[1] == "fibo":
    high = float(sys.argv[2])
    low = float(sys.argv[3])
    trend = str(sys.argv[4])
    print(Fib(high, low, trend))

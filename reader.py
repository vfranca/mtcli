#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cli_trade.cli_trade import controller
from cli_trade.settings import *
import sys, re


file = csv_path

pattern_qtt = re.compile(r'^[0-9]*$')
pattern_date = re.compile(r'^[0-9]{4}.[0-9]{2}.[0-9]{2}$')
pattern_view = re.compile('^[a-z]*$')

# chamada com 1 argumento
if len(sys.argv) == 2:
    file += sys.argv[1]
    views = controller(file)

# chamada com 2 argumentos
elif len(sys.argv) == 3:
    file += sys.argv[1]
    arg2 = sys.argv[2]
    if pattern_qtt.match(arg2):
        views = controller(file, qtt_bars = int(arg2))
    elif pattern_date.match(arg2):
        views = controller(file, date = arg2)
    elif pattern_view.match(arg2):
        views = controller(file, view = arg2)

# chamada com 3 argumentos
elif len(sys.argv) == 4:
    file += sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]

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

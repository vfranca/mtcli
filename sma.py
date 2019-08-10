#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cli_trade.sma import ma
from cli_trade.settings import *
import sys


times = int(sys.argv[1])
filename = csv_path + sys.argv[2]

mms = ma(times, filename)
print(mms)


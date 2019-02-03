@echo off
set f="%win%m15.csv"
set mm="ema"
py %mm%.py 17 %f%
py %mm%.py 34 %f%
py %mm%.py 72 %f%

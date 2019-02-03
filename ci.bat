@echo off
set f="%win%%1.csv"
set mm="ema"
py %mm%.py 8 %f%
py %mm%.py 17 %f%

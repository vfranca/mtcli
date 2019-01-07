@echo off
set f="wing19m5.csv"
set mm="ema"
py %mm%.py 8 %f%
py %mm%.py 17 %f%

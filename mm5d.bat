@echo off
set file="wdog19m5.csv"
py sma.py 8 %file%
py sma.py 17 %file%

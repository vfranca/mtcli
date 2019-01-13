@echo off
set file="wdog19m10.csv"
py sma.py 8 %file%
py sma.py 17 %file%
py sma.py 34 %file%
py sma.py 72 %file%

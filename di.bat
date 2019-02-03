@echo off
set f=%1.csv
set mm="sma"
py %mm%.py 3 %f%
py %mm%.py 8 %f%
py %mm%.py 20 %f%

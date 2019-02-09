@echo off
set f=%t%%1.csv
py %mm%.py 3 %f%
py %mm%.py 8 %f%
py %mm%.py 20 %f%
time /t

@echo off
py reader.py %t%%1.csv %2 %3
time /t
rem py sma.py 20 %t%%1%.csv

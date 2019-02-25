@echo off
py reader.py %t%%1.csv brooks %2
py sma.py 20 %t%%1%.csv
time /t

@echo off
set file=%t%weekly.csv
py reader.py %file% %*
py sma.py 20 %file%
time /t
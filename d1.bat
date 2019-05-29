@echo off
set file=%t%daily.csv
py reader.py %file% %*
py ema.py 20 %file%
time /t

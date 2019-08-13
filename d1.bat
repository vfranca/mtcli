@echo off
set file=%t%daily.csv
py manage.py bars %file% %*
py manage.py ema 20 %file%
time /t

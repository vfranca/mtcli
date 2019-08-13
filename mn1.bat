@echo off
set file=%t%monthly.csv
py manage.py bars %file% %*
py manage.py ema 20 %file%

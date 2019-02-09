@echo off
set file=%t%daily.csv
py reader.py %file% %*
rem del var\%file%
time /t

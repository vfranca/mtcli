@echo off
set file=%t%daily.csv
rem py reader.py %file% %*
b daily %*
rem del var\%file%
time /t

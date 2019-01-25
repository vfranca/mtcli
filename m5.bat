@echo off
set file=%WIN%m5.csv
py reader.py %file% %*
rem del var\%file%
time /t

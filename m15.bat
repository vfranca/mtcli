@echo off
set file=%WIN%m15.csv
py reader.py %file% %*
rem del var\%file%
time /t

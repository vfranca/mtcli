@echo off
set file=%WIN%m10.csv
py reader.py %file% %*
rem del var\%file%
time /t

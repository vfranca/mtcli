@echo off
set file=%WIN%m30.csv
py reader.py %file% %*
rem del var\%file%
time /t

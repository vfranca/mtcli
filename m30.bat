@echo off
set file=%WIN%m30.csv
py reader.py %file% 109 %*
rem del var\%file%
time /t

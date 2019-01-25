@echo off
set file=%WIN%h4.csv
py reader.py %file% %*
rem del var\%file%
time /t

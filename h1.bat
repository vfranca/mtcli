@echo off
set file=%WIN%h1.csv
py reader.py %file% %*
rem del var\%file%
time /t

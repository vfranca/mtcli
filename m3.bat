@echo off
set file=%WIN%m3.csv
py reader.py %file% 109
del var\%file%
time /t

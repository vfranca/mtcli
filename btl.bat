@echo off
REM Binary Logic Trend
REM acima de 17 = 1
REM Acima de 72 = 2
REM Acima de 305 = 4
if "%1" == "" (
    py reader.py %t%daily.csv c 1
    py %mm%.py 17 %t%daily.csv
    py %mm%.py 72 %t%daily.csv
    py %mm%.py 305 %t%daily.csv
) else (
    py reader.py %t%%1.csv c 1
    py %mm%.py 17 %t%%1.csv
    py %mm%.py 72 %t%%1.csv
    py %mm%.py 305 %t%%1.csv
)

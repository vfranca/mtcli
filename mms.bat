@echo off
set mm="sma"
if "%2" == "" (
    py %mm%.py 17 %1.csv
    py %mm%.py 34 %1.csv
    py %mm%.py 72 %1.csv
    goto :EOF
) else (
    py %mm%.py %1 %2.csv
    goto :EOF
)

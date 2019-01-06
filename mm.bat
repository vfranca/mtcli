@echo off
if "%2" == "" (
    py sma.py 17 %1.csv
    py sma.py 34 %1.csv
    py sma.py 72 %1.csv
    goto :EOF
) else (
    py sma.py %1 %2.csv
    goto :EOF
)

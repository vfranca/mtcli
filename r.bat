@echo off
if "%2" == "" (
    py reader.py %1.csv 10
    goto :EOF
) else (
    py reader.py %1.csv %2
    goto :EOF
)

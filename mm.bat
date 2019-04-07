@echo off
if "%2" == "" (
    py %mm%.py 20 %t%%1.csv
    py %mm%.py 200 %t%%1.csv
    goto :EOF
) else (
    py %mm%.py %2 %t%%1.csv
    goto :EOF
)


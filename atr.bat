@echo off

if "%1" == "win" (
    py atr.py %WIN%%2 %3
    goto :EOF
    )

if "%1" == "wdo" (
    py atr.py %WDO%%2 %3
    goto :EOF
    )

py atr.py %1 %2

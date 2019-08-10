@echo off
rem ema.bat - Exibe a média móvel exponencial
rem Valmir França - vfranca3@gmail.com
if "%2" == "" (
	py ema.py 20 %t%%1.csv
) else (
	py ema.py %2 %t%%1.csv
)


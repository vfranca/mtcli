@echo off
rem sma.bat - Exibe a média móvel aritmética
rem Valmir França - vfranca3@gmail.com
if "%2" == "" (
	py sma.py 20 %t%%1.csv
) else (
	py sma.py %2 %t%%1.csv
)


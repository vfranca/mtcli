@echo off
if "%2" == "" (
	py manage.py sma 20 %t%%1.csv
) else (
	py manage.py sma %2 %t%%1.csv
)


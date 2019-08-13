@echo off
if "%2" == "" (
	py manage.py ema 20 %t%%1.csv
) else (
	py manage.py ema %2 %t%%1.csv
)


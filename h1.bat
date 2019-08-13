@echo off
set tf=h1
if %d% == "" (
	py manage.py bars %t%%tf%.csv %*
) else (
	py manage.py %t%%tf%.csv %d% %*
)
py manage.py ema 20 %t%%tf%.csv

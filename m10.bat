@echo off
set tf=m10
if %d% == "" (
	py reader.py %t%%tf%.csv %*
) else (
	py reader.py %t%%tf%.csv %d% %*
	)
py ema.py 20 %t%%tf%.csv
time /t

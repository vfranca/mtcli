@echo off
set tf=m15
py reader.py %t%%tf%.csv %d% %*
py ema.py 20 %t%%tf%.csv
time /t

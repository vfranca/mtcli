@echo off
set tf=m5
py reader.py %t%%tf%.csv %d% %*
py ema.py 20 %t%%tf%.csv
time /t

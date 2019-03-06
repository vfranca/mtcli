@echo off
set tf=h1
py reader.py %t%%tf%.csv %d% %*
py ema.py 20 %t%%tf%.csv
rem atr h1
rem time /t

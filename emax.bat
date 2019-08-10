@echo off
rem emax.bat Médias móveis exponenciais para Day Trade
rem 20 períodos de M5, M15, H1 e D1
rem Valmir França - vfranca3@gmail.com
py reader.py %t%daily.csv c 1
py ema.py 20 %t%m5.csv
py ema.py 20 %t%m15.csv
py ema.py 20 %t%h1.csv
py ema.py 20 %t%daily.csv

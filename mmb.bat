@echo off
rem Médias Móveis de Brooks
set mm=ema
py %mm%.py 20 %t%m5.csv
py %mm%.py 20 %t%m15.csv
py %mm%.py 20 %t%%h1.csv

@echo off
rem Médias móveis para Swing trade
bars %t% -p daily -v c -c 1
sma %t% -p daily -c 20
sma %t% -p daily -c 50
sma %t% -p daily -c 200

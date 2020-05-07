@echo off
bars %t% -p daily -v c -c 1
sma %t% -p daily -c 9
sma %t% -p daily -c 20

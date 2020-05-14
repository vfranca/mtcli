@echo off
rem aliases para comandos do mtcli
rem grafico de ranges
set p=m5
mt bars %t% --view r --period %p% --date %d% --count 107

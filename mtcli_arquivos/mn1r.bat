@echo off
rem aliases para comandos do mtcli
rem grafico de ranges
set p=monthly
mt bars %t% --view r --period %p% --count 107

@echo off
rem deprecated
rem aliases para comandos do mtcli
rem grafico de ranges
set p=daily
mt bars %t% --view r --period %p% --count 107

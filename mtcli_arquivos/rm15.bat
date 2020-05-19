@echo off
rem deprecatedrem aliases para comandos do mtcli
rem grafico de ranges
set p=m15
mt bars %t% --view r --period %p% --date %d% --count 107

@echo off
rem aliases para comandos do mtcli
rem gráfico default
cls
if "%1" == "" (
mt bars %t% --period %p% --date %d% --count 108
) else (
mt bars %t% --period %p% --date %d% --view %1 --count %2
)
mt sma %t% --period %p% --count 20
time /t

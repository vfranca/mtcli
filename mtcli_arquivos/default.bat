@echo off
rem aliases para comandos do mtcli
rem view default
if "%1" == "" (
mt bars %t% --period %p% --date %d% --count 107
) else (
mt bars %t% --period %p% --date %d% --view %1 --count %2
)
mt sma %t% --period %p% --count 20

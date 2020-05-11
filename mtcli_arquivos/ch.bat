@echo off
rem aliases para comandos do mtcli
rem chamada da view channel
if "%1" == "" (
echo mt bars %t% --period %p% --date %d% --view ch --count 107
mt bars %t% --period %p% --date %d% --view ch --count 107
) else (
echo mt bars %t% --period %p% --date %d% --view %1 --count %2
mt bars %t% --period %p% --date %d% --view %1 --count %2
)
mt sma %t% --period %p% --count 20

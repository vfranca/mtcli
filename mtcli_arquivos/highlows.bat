@echo off
rem aliases para comandos do mtcli
rem grafico de máximas e mínimas
cls
rem Exibe o comando do alias
if "%1" == "-e" (
echo mt bars %t% --period %p% --date %d% --view ch --count 108
echo mt sma %t% --period %p% --count 20
goto :EOF
)
if "%3" == "-e" (
echo mt bars %t% --period %p% --date %d% --view %1 --count %2
echo mt sma %t% --period %p% --count 20
goto :EOF
)
if "%1" == "" (
mt bars %t% --period %p% --date %d% --view ch --count 108
) else (
mt bars %t% --period %p% --date %d% --view %1 --count %2
)
mt sma %t% --period %p% --count 20
time /t

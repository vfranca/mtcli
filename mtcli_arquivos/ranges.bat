@echo off
rem aliases para comandos do mtcli
rem gráfico de ranges
cls
rem Exibe o comando do alias
if "%1" == "-e" (
echo mt bars %t% --period %p% --date %d% --view r --count 108
echo mt atr %t% --period %p%
goto :EOF
)
mt bars %t% --period %p% --date %d% --view r --count 108
mt atr %t% --period %p%

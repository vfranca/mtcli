@echo off

rem interação com mtcli
rem chamada da view channel

if "%1" == "" (
bars %t% -p %p% -d %d% -v ch
) else (
bars %t% -p %p% -d %d% -v %1 -c %2
)
sma %t% -p %p% -c 20

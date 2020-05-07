@echo off

rem interação com o mtcli
rem view default

if "%1" == "" (
bars %t% -p %p% -d %d%
) else (
bars %t% -p %p% -d %d% -v %1 -c %2
)
sma %t% -p %p% -c 20


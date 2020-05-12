@echo off
rem aliases para comandos do mtcli
set default=u20

if "%1" == "" (
call a ccm%default%
goto :EOF
)

if "%1" == "$" (
call a ccm$n
goto :EOF
)

if "%1" == "-s" (
echo F Janeiro
echo H Marco
echo K Maio
echo N Julho
echo U Setembro
echo V Outubro
echo Z Dezembro
goto :EOF
)

call a ccm%120

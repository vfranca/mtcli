@echo off
rem aliases para comandos do mtcli
set default=m20

if "%1" == "" (
call a win%default%
goto :EOF
)

if "%1" == "$" (
call a win$n
goto :EOF
)

if "%1" == "-s" (
echo G Fevereiro
echo J Abril
echo M Junho
echo Q Agosto
echo V Outubro
echo Z Dezembro
goto :EOF
)

call a win%120

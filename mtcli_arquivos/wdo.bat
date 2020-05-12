@echo off
rem aliases para comandos do mtcli
set default=m20

if "%1" == "" (
call a wdo%default%
goto :EOF
)

if "%1" == "$" (
call a wdo$n
goto :EOF
)

if "%1" == "-s" (
echo G Janeiro
echo H Fevereiro
echo J Marco
echo K Abril
echo M Maio
echo N Junho
echo Q Julho
echo U Agosto
echo V Setembro
echo X Outubro
echo Z Novembro
echo F Dezembro
goto :EOF
)

call a wdo%120

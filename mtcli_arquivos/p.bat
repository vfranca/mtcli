@echo off
rem aliases para comandos do mtcli
rem exibe/define a variável period

if "%1" == "" (
echo %p%
goto :EOF
)

set p=%1%

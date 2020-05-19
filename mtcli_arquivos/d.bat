@echo off
@rem aliases para comandos do mtcli
if "%1" == "" (
set d=""
echo date %d%
goto :EOF
)
set d=%3.%2.%1
echo date %d%

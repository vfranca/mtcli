@echo off
rem aliases para comandos do mtcli
rem exibe/define a variável s

if "%1" == "" (
echo %t%
goto :EOF
)

set t=%1
title %1


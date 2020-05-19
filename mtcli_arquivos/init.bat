@echo off
rem deprecated
rem aliases para comandos do mtcli
rem lista as variáveis de ambiente
if "%1" == "-l" (
echo symbol %t%
echo period %p%
echo date %d%
goto :EOF
)

rem inicia as variáveis de ambiente
set t=petr4
echo symbol PETR4
set p=m15
echo period Daily
set d=""
echo data vazio
prompt $$
echo alterado prompt
title mtcli
echo alterado titulo do terminal
echo diretorio pronto para trabalho

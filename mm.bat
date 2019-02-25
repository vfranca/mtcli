@echo off
rem uso
rem Exemplo 1:
rem mm %t%m5
rem exibe as médias mmóveis de 17, 34 e 72 períodos do ativo
rem exemplo 2:
rem mm %t%m5 21
rem Exibe a média móvel de 21 períodos do ativo
if "%2" == "" (
    py %mm%.py 17 %t%%1.csv
    py %mm%.py 34 %t%%1.csv
    py %mm%.py 72 %t%%1.csv
    py %mm%.py 144 %t%%1.csv
    py %mm%.py 305 %t%%1.csv
    py %mm%.py 610 %t%%1.csv
    rem py %mm%.py 1292 %t%%1.csv
    rem py %mm%.py 20 %t%%1.csv
    rem py %mm%.py 60 %t%%1.csv
    rem py %mm%.py 240 %t%%1.csv
    goto :EOF
) else (
    py %mm%.py %2 %t%%1.csv
    goto :EOF
)


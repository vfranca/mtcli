@echo off
rem Médias móveis para Day Trade
rem preço atual do ativo
bars %t% --period daily --view c --count 1
rem média móvel de 20 períodos do 5 min
sma %t% --period m5 --count 20
rem média móvel de 60 períodos do m5
rem equivale à média móvel de 20 períodos do 15 min
sma %t% --period m5 --count 60
rem média móvel de 240 períodos do m5
rem equivale à média móvel de 20 períodos do h1
sma %t% --period m5 --count 240

# mm
Exibe a média móvel simples.  
  
## sintaxe
mt mm [--period <periodo>] [--count <quantidade>] <ativo>  
  
## opções

### --period, -p
define o timeframe  

valor | descrição
:--- | :-----
m1 | 1 min
m2 | 2 min
m3 | 3 min
m4 | 4 min
m5 | 5 min
m6 | 6 min
m10 | 10 min
m12 | 12 min
m15 | 15 min
m20 | 20 min
m30 | 30 min
h1 | 1h
h2 | 2h
h3 | 3h
h4 | 4h
d1 | diário
w1 | semanal
mn1 | mensal

exemplo:
```cmd
mt mm --period d1  eurusd
```

### --count, -c
Define a quantidade de barras calculadas.  

exemplo:  
```cmd
mt mm --period d1 --count 20 eurusd
``` 
  
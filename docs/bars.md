# bars
Exibe as barras do gráfico de candles.  
  
## sintaxe
mt bars [--period <periodo>] [--count <quantidade>] [--view <visao>] [--date <data>] <ativo>  
  
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
mt bars --period d1 eurusd
```

### --count, -c
Define a quantidade de barras a serem exibidas.  

exemplo:  
```cmd
mt bars --count 100 eurusd
``` 
  
### --view, -v
Define a forma como cada barra será exibida.  

valor | descrição
:---- | :----
default | completo
ch | mínimo
r | ranges
c | fechamentos
l | mínimas
h | máximas
var | variação percentual
oh | OHLC

exemplo:  
```cmd
mt bars -v ch eurusd
```

# bars
Exibe as barras do gráfico de candles  
  
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
exemplo:
```cmd
mt bars eurusd --period d1
```

### --count, -c
Define a quantidade de barras a serem exibidas
exemplo:
```cmd
mt bars eurusd --count 100
``` 
  
### --view, -v
Define a forma como cada barra será exibida.  
valor | descrição
:---- | :----
ch | mínimo
r | ranges
c | fechamentos
l | mínimas
h | máximas
var | variação percentual
oh | OHLC
exemplo
```cmd
mt bars eurusd -v ch

# mtcli

## [mt bars  ](#)
Exibe as barras do gráfico.  
```
> mt bars <symbol> [--view <ch>] [--period <period>] [--count <count>] [--date <date>]  
```
Exibe as barras do gráfico do ativo na view, no período, na quantidade e na data especificada.  
Exemplo:  
```
> mt bars wing20 --view b --period h1 --count 1 --date 2020.02.10
```
Resultado:  
10 ASC CP VERDE86R250.00 G215.00 BOTTOM14 113105.00 112815.00 113105.00MP112960.00 R290.00 0.22  


## [mt sma](#)  
Exibe a média móvel simples.  
```
> mt sma <wing20> [--period <period>] [--count <count>]
```
Exemplo:  
```
> mt sma wing20 --period h1 --count 20
```
Resultado:  
113623.0


## [mt ema](#)  
Exibe a média móvel exponencial.  
```
> mt ema <wing20> [--period <period>] [--count <count>]
```
Exemplo:  
```
> mt ema wing20 --period h1 --count 20
```
Resultado:  
113670.85  


## [mt atr](#)  
Exibe o average true range de 14 períodos.  
```
> mt atr <wing20> [--period <period>] [--count <count>]
```
Exemplo:  
```
> mt atr wing20 --period h1
```
Resultado:  
583.21  


## [mt fib](#)  
Exibe retrações e projeções de fibonacci.  
```
> mt fib <maxima> <minima> <direção>
```
Exemplo:  
```
> mt fib 120080 105625 h
```
Resultado:  
117326.81 117852.50 118378.19 > 121781.81 122307.50 122833.19

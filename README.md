# CLI Trade

Provê uma interface de linha de comando para ler gráficos de preços gerados pelo MetaTrader 5

## Pré-requisitos  
* MetaTrader 5  
* Python 3  

## Exemplos de uso  
```
> py reader.py winq19daily.csv 20  
Exibe as últimas 20 barras do diário do winq19.  
> py reader.py winq19daily.csv ch 20  
Exibe o canal das últimas 20 barras do diário do winq19.  
> py reader.py winq19daily.csv o 20  
Exibe o preço de abertura das últimas 20 barras do diário do winq19.  
> py reader.py winq19daily.csv c 20  
Exibe o preço de fechamento das últimas 20 barras do diário do winq19.  
> py reader.py winq19daily.csv h 20  
Exibe o preço máximo das últimas 20 barras do diário do winq19.  
> py reader.py winq19daily.csv l 20  
Exibe o preço mínimo das últimas 20 barras do diário do winq19.  
> py reader.py winq19daily.csv r 20  
Exibe o range das últimas 20 barras do diário do winq19.  
> py reader.py winq19daily.csv vol 20  
Exibe o volume das últimas 20 barras do diário do winq19.  

> py atr.py winq19daily  
Exibe o ATR(14) do diário do winq19.  
> py atr.py winq19 20  
Exibe o ATR(20) do diário do winq19.  

> py sma.py 20 winq19daily.csv  
Exibe a média móvel aritmética de 20 períodos do diário do winq19.  
> py ema.py 20 winq19daily.csv  
Exibe a média móvel exponencial de 20 períodos do diário do winq19.  

> py fibo.py 103900 102100 h  
Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de alta.  
> py fibo.py 103900 102100 l  
Exibe as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de baixa.  
```

## Arquivos em lote  

Os arquivos em lote é uma forma de fornecer aliases para os comandos em Python.  
Exemplos:  
```
> m5  
Exibe as barras do 5 minutos do ativo definido na variável de ambiente %t% 
> m15 c  
Exibe os preços de fechamento das barras do 15 min do ativo definido na variável de ambiente %t%.  
> ema h1  
Exibe a média móvel exponencial de 20 períodos do 60 minutos do ativo definido na variável de ambiente %t%.  
> atr daily  
Exibe o ATR(14) do diário.  
> f 103900 102100 l  
Exibe os números de fibonacci entre os preços na tendência de baixa.  
```







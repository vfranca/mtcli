# mtcli Arquivos

Arquivos de trabalho do mtcli. Descompacte em uma pasta separada para o mtcli.  

## Experts Advisors  

Os experts advisors (robôs) localizados na pasta experts deverão ser anexados aos gráficos do MetaTrader.  
EAs disponíveis:  

* GeraCSVDayTrade.ex5 - Tempos gráficos para day trading.
* GeraCSVDayTrade.ex5 - Tempos gráficos para day trading (m1 a m5, m10, m15, h1, h4 e daily).
* GeraCSVSwingTrade.ex5 - Tempos gráficos para swing trading (m15, h1, daily, weekly e monthly).
* experts/GeraCSVBackTest.ex5 - Tempos gráficos para backtesting (m5, m10, m15, h1 e daily).

## Arquivo .env  

O arquivo .env deve ser colocado em C:\.env e deve ser alterado com a informação do caminho da pasta de dados do MetaTrader5 em seu sistema.


## Atalhos  

Os arquivos em lote (.bat) são atalhos para os comandos do mtcli e antes de serem usados deverá executar o arquivo conf.bat. Execute no prompt de comando:
```
> conf
```
Para definir o ativo objeto da exibição dos dados do gráfico:  
```
> s petr4  
```
Para exibir o gráfico padrão do diário:    
```
> dd1  
Para exibir o gráfico de máximas e mínimas do diário:  
```
> d1  
```
```
Para exibir as médias móveis do diário de 20, de 50 e de 200 períodos:  
```
> mmd1
```
Para exibir as médias móveis do m5 de 20, de 60 e de 240 períodos:  
```
> mmm5
```

# mtcli  
  
Aplicativo CLI para exibir o gráfico de barras do MetaTrader 5 em texto.  
O formato texto pode ser lido pelo leitor de telas NVDA.  
O mtcli é uma aplicação feita por um deficiente visual para deficientes visuais.
  
## Pré-requisitos  

* Plataforma de negociação MetaTrader 5.  
* Leitor de tela NVDA.  

obs.: O mtcli não foi testado com outros leitores de tela além do NVDA.  
    

## Instalação  

### Executável

[Clique aqui para baixar o executável](https://bit.ly/mtcli)
  
Descompacte  a pasta e execute:  
```
cd mtcli
mt --version
```
deverá exibir algo como mtcli 0.31.2

A pasta contem dois aplicativos do MetaTrader 5: Mtcli.ex5 e MA_TXT.ex5.  

* O Mtcli.ex5 exporta as cotações em CSV, e é necessário para que os comandos do mtcli possam ser executados
* O MA_TXT.ex5 exporta as médias móveis em CSV, e é necessário para que o comando mt ma possa ser executado
  
Eles deverão ser anexados ao gráfico do MetaTrader 5 para que o mtcli possa ler esses dados
  
Digite mt --help para obter uma ajuda rápida e uma  lista de subcomandos disponíveis:
```
mt --help
```
Para uma ajuda para cada subcomando execute mt <subcomando> --help

### Python

Outra forma de obter o mtcli é pelo índice de pacotes do python (PyPI).  
Se você tiver o python instalado e disponível no prompt de comando execute o seguinte comando para instalar o mtcli:  
```
pip install mtcli
```

## Comandos  
  
| Comando | Descrição | Exemplo |
| :----- | :------ | :---- |
| [mt bars](bars.md) | Exibe o gráfico de candlestick. | mt bars IBOV |
| [mt mm](mm.md) | Calcula a média móvel simples. | mt mm IBOV |
| [mt rm](rm.md) | Calcula o tamanho médio das barras.| mt rm IBOV |
| mt conf | Gerencia configurações do mtcli | mt conf |
  
## abreviaturas  

[Clique aqui para ver uma lista de abreviaturas exibidas nas barras](abreviaturas.md)  

## Agradecimentos  
  
Ao @MaiconBaggio fornecedor do primeiro EA exportador das cotações para CSV.  
Ao Claudio Garini que transferiu a exportação das cotações para um indicador.  
